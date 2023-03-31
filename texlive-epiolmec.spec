Name:		texlive-epiolmec
Version:	15878
Release:	2
Summary:	Typesetting the Epi-Olmec Language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/epiolmec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epiolmec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epiolmec.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epiolmec.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains all the necessary files to typeset Epi-
Olmec ``documents'', a script used in Southern Middle America
until about 500 AD.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/epiolmec/epiolmec.map
%{_texmfdistdir}/fonts/tfm/public/epiolmec/EpiOlmec.tfm
%{_texmfdistdir}/fonts/type1/public/epiolmec/Epi-Olmec.pfb
%{_texmfdistdir}/tex/latex/epiolmec/epiolmec.sty
%doc %{_texmfdistdir}/doc/latex/epiolmec/GlyphAccessCommands.pdf
#- source
%doc %{_texmfdistdir}/source/latex/epiolmec/epiolmec.dtx
%doc %{_texmfdistdir}/source/latex/epiolmec/epiolmec.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
