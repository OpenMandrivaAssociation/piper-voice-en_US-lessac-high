Name:		piper-voice-en_US-lessac-high
Version:	2023.09.23
Release:	1
Summary:	US English female voice for the Piper TTS system, high quality (but bigger file)
URL:		https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US/lessac/high
License:	MIT
BuildArch:	noarch
Group:		System/Multimedia
Provides:	piper-voice
Provides:	piper-voice-en
Provides:	piper-voice-en_US

%sourcelist
https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/high/en_US-lessac-high.onnx
https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/high/en_US-lessac-high.onnx.json

%description
%{summary}

%install
mkdir -p %{buildroot}%{_datadir}/piper/voices
install -c -m 644 %{S:0} %{S:1} %{buildroot}%{_datadir}/piper/voices/

%files
%{_datadir}/piper/voices/*
