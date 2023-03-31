Name:		texlive-xpdfopen
Version:	53998
Release:	2
Summary:	Commands to control PDF readers, under X11
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xpdfopen
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpdfopen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpdfopen.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The command-line programs pdfopen and pdfclose allow you to
control the X Window System version of Adobe's Acrobat Reader
from the command line or from within a (shell) script. The
programs work with Acrobat Reader 5, 7, 8 and 9 for Linux, xpdf
and evince. This version derives from one written by Fabrice
Popineau for Microsoft operating systems.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdfopen.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdfopen.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdfclose.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdfclose.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
