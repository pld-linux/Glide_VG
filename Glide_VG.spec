Summary:	Glide runtime for 3Dfx Voodoo Graphics boards
Summary(pl):	¶rodowisko Glide dla kart 3Dfx Voodoo Graphics
Name:		Glide_VG
Version:	2.46
Release:	4
License:	3DFX GLIDE Source Code General Public License
Vendor:		3Dfx Interactive Inc.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	Glide%{version}.tar.gz
Patch0:		%{name}-asm.patch
Icon:		3dfx.gif
URL:		http://www.3dfx.com	
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows the user to use a 3Dfx Interactive Voodoo Graphics
card under Linux.

%description -l pl
Ten pakiet pozwala na uøywanie kart 3Dfx Interactive Voodoo Graphics
pod Linuksem.

%package -n Glide2x_SDK
Summary:	Development libraries for Glide 2.x
Summary(pl):	CzÍ∂Ê Glide 2.x przeznaczona dla programistÛw
Version:	2.1
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description -n Glide2x_SDK
This package includes the headers files, documentation, and test files
necessary for developing applications that use the 3Dfx Interactive
Voodoo Graphics, Voodoo Rush, or Voodoo2 card.

%description -n Glide2x_SDK -l pl
Ten pakiet zawiera pliki nag≥Ûwkowe, dokumentacjÍ i pliki testowe
potrzebne do tworzenia aplikacji uøywaj±cych kart 3Dfx Interactive
Voodoo Graphics, Voodoo Rush lub Voodoo2.

%prep
%setup -q -c
%patch -p1
chmod +x swlibs/include/make/ostype

%build
%{__make} -f makefile.unix CNODEBUG="%{rpmcflags} %{!?debug:-fomit-frame-pointer} \
	%{!?debug:-funroll-loops -fexpensive-optimizations -ffast-math} -I%{_prefix}/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/glide}
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/{tests,texus/{lib,cmd,examples}}

# Install the glibc 2.1 libraries normally
install sst1/lib/libglide2x.so $RPM_BUILD_ROOT%{_libdir}/libglide2x_VG.so
install swlibs/lib/libtexus.so $RPM_BUILD_ROOT%{_libdir}
ln -sf libglide2x_VG.so $RPM_BUILD_ROOT%{_libdir}/libglide2x.so

# Install the executables
install swlibs/bin/texus $RPM_BUILD_ROOT%{_bindir}
install sst1/glide/tests/test00 $RPM_BUILD_ROOT%{_bindir}/test3Dfx

# Install the headers
install swlibs/include/3dfx.h $RPM_BUILD_ROOT%{_includedir}/glide
install sst1/include/glide.h $RPM_BUILD_ROOT%{_includedir}/glide
install sst1/include/glidesys.h $RPM_BUILD_ROOT%{_includedir}/glide
install sst1/include/glideutl.h $RPM_BUILD_ROOT%{_includedir}/glide
install sst1/include/sst1vid.h $RPM_BUILD_ROOT%{_includedir}/glide
install sst1/include/gump.h $RPM_BUILD_ROOT%{_includedir}/glide
install swlibs/include/linutil.h $RPM_BUILD_ROOT%{_includedir}/glide
install swlibs/include/texus.h $RPM_BUILD_ROOT%{_includedir}/glide

# Install the examples and their source
install sst1/glide/tests/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests/makefile
install sst1/glide/tests/*.3df $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests
install sst1/glide/tests/test??.c $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests
install sst1/glide/tests/tldata.inc $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests
install sst1/glide/tests/tlib.[ch] $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/tests

# Install the texture tools source
install swlibs/texus/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/makefile
install swlibs/texus/lib/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/lib/makefile
install swlibs/texus/cmd/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/cmd/makefile
install swlibs/texus/examples/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/examples/makefile
install swlibs/texus/lib/*.c $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/lib
install swlibs/texus/lib/texusint.h $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/lib
install swlibs/texus/cmd/*.c $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/cmd
install swlibs/texus/examples/*.c $RPM_BUILD_ROOT%{_prefix}/src/examples/glide/texus/examples

gzip -9nf glide_license.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc glide_license.txt.gz
%attr(755,root,root) %{_bindir}/texus
%attr(755,root,root) %{_bindir}/test3Dfx
%attr(755,root,root) %{_libdir}/libglide2x.so
%attr(755,root,root) %{_libdir}/libglide2x_VG.so
%attr(755,root,root) %{_libdir}/libtexus.so

%files -n Glide2x_SDK
%defattr(644,root,root,755)
%doc docs/*.pdf
%{_prefix}/src/examples/glide
%{_includedir}/glide
