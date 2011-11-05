# revision 23537
# category Package
# catalog-ctan /macros/latex/contrib/undolabl
# catalog-date 2011-08-12 14:47:20 +0200
# catalog-license lppl1.3
# catalog-version 1.0j
Name:		texlive-undolabl
Version:	1.0j
Release:	1
Summary:	Override existing labels
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/undolabl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/undolabl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/undolabl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/undolabl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package allows the user to override existing labels (for
example, those generated automatically).

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
%{_texmfdistdir}/tex/latex/undolabl/undolabl.sty
%doc %{_texmfdistdir}/doc/latex/undolabl/README
%doc %{_texmfdistdir}/doc/latex/undolabl/undolabl-example.pdf
%doc %{_texmfdistdir}/doc/latex/undolabl/undolabl-example.tex
%doc %{_texmfdistdir}/doc/latex/undolabl/undolabl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/undolabl/undolabl.drv
%doc %{_texmfdistdir}/source/latex/undolabl/undolabl.dtx
%doc %{_texmfdistdir}/source/latex/undolabl/undolabl.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
