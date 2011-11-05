# revision 15878
# category Package
# catalog-ctan /language/epiolmec
# catalog-date 2007-02-06 22:00:42 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-epiolmec
Version:	20070206
Release:	1
Summary:	Typesetting the Epi-Olmec Language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/epiolmec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epiolmec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epiolmec.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epiolmec.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package contains all the necessary files to typeset Epi-
Olmec ``documents'', a script used in Southern Middle America
until about 500 AD.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
