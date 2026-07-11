%global tl_name undolabl
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0o
Release:	%{tl_revision}.1
Summary:	Override existing labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/undolabl
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/undolabl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/undolabl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/undolabl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to override existing labels (for example,
those generated automatically).

