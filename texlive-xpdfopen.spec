%global tl_name xpdfopen
%global tl_revision 65952

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.86
Release:	%{tl_revision}.1
Summary:	Commands to control PDF readers, under X11
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/xpdfopen
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpdfopen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpdfopen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(xpdfopen.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The command-line programs pdfopen and pdfclose allow you to control the
X Window System version of Adobe's Acrobat Reader from the command line
or from within a (shell) script. The programs work with Acrobat Reader
5, 7, 8 and 9 for Linux, xpdf and evince. This version derives from one
written by Fabrice Popineau for Microsoft operating systems.

