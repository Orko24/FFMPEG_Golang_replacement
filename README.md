# FFMPEG_Golang_replacement
Open Source Project to create Go based FFMPEG alternative 

This repository/code base was designed to be an open source alternative to FFPMEG. 

Throughout the project lifetime of the Adamas Project, a conflict between https://github.com/Zulko/moviepy and IBM Cloud/ Azure based services. This resulted in audio data not being abled to be processed without a remote desktop connection (RDP) from a cloud computing perspective. 

My hypothesis is the frameworks involved Django, Apache and FFMPEG all conflict with each other as their written in C and C is a functional language not an OOP language thus has limited data pipelining capabilities.

Thus in order to combat this I've written an API to integrate a Golang or C++ solution into a Pythonic framework so it can effectively be used like any other packages to build high level programs or scale with existing ones. 

Enjoy!
