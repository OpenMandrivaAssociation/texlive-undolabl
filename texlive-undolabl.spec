Name:		texlive-undolabl
Version:	36681
Release:	1
Summary:	Override existing labels
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/undolabl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/undolabl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/undolabl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/undolabl.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to override existing labels (for
example, those generated automatically).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
