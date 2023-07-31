#include <sox.h>
#include <memory>

sox_signalinfo_t _intermediateSignal;
sox_format_t *input;
sox_format_t *output;
sox_effects_chain_t *effectsChain;

void addEffect(std::string effectName, sox_format_t *options)
{
    std::unique_ptr<sox_effect_t> effect(sox_create_effect(sox_find_effect(effectName.c_str())));
    char *args[] = {reinterpret_cast<char *>(options)};
    sox_effect_options(effect.get(), 1, args);
    sox_add_effect(effectsChain, effect.get(), &_intermediateSignal, &input->signal);
}

int main()
{
    if (sox_init() != SOX_SUCCESS)
        throw std::runtime_error("Could not initialise SOX.");

    input = sox_open_read("default", NULL, NULL, "alsa");
    output = sox_open_write("recorded.wav", &input->signal, NULL, NULL, NULL, NULL);
    if (!input || !output)
        throw std::runtime_error("SOX I/O error");

    _intermediateSignal = input->signal;

    effectsChain = sox_create_effects_chain(&input->encoding, &output->encoding);

    if (!effectsChain)
        throw std::runtime_error("SOX could not initialize effects chain.");

    addEffect("input", input);
    addEffect("output", output);

    sox_flow_effects(effectsChain, NULL, NULL);
    sox_quit();
}