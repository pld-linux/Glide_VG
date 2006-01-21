Summary:	Glide runtime for 3Dfx Voodoo Graphics boards
Summary(pl):	¦rodowisko Glide dla kart 3Dfx Voodoo Graphics
Name:		Glide_VG
Version:	2.46
Release:	9
License:	3DFX GLIDE Source Code General Public License
Vendor:		3Dfx Interactive Inc.
Group:		Libraries
Source0:	Glide%{version}.tar.gz
# Source0-md5:	be7762636b46cb04b238a16f45cfcfa8
Patch0:		%{name}-asm.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-morearchs.patch
Patch3:		%{name}-ioctl.patch
Patch4:		%{name}-soname.patch
Patch5:		%{name}-C_brainos.patch
URL:		http://www.3dfx.com/
%ifarch %{ix86}
BuildRequires:	/usr/bin/gasp
%endif
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows the user to use a 3Dfx Interactive Voodoo Graphics
card under Linux.

%description -l pl
Ten pakiet pozwala na u¿ywanie kart 3Dfx Interactive Voodoo Graphics
pod Linuksem.

%package -n Glide2x_SDK
Summary:	Development libraries for Glide 2.x
Summary(pl):	Czê¶æ Glide 2.x przeznaczona dla programistów
Version:	2.1
Group:		Development/Libraries

%description -n Glide2x_SDK
This package includes the headers files, documentation, and test files
necessary for developing applications that use the 3Dfx Interactive
Voodoo Graphics, Voodoo Rush, or Voodoo2 card.

%description -n Glide2x_SDK -l pl
Ten pakiet zawiera pliki nag³ówkowe, dokumentacjê i pliki testowe
potrzebne do tworzenia aplikacji u¿ywaj±cych kart 3Dfx Interactive
Voodoo Graphics, Voodoo Rush lub Voodoo2.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
chmod +x swlibs/include/make/ostype

%build
%{__make} -j1 -f makefile.unix \
	CNODEBUG="%{rpmcflags} -fPIC %{!?debug:-fomit-frame-pointer} \
	%{!?debug:-funroll-loops -fexpensive-optimizations -ffast-math} -I/usr/X11R6/include" \
%ifnarch %{ix86}
	FX_GLIDE_CTRISETUP=1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/glide} \
	$RPM_BUILD_ROOT%{_examplesdir}/glide/{tests,texus/{lib,cmd,examples}}

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
install sst1/glide/tests/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/tests/makefile
install sst1/glide/tests/*.3df $RPM_BUILD_ROOT%{_examplesdir}/glide/tests
install sst1/glide/tests/test??.c $RPM_BUILD_ROOT%{_examplesdir}/glide/tests
install sst1/glide/tests/tldata.inc $RPM_BUILD_ROOT%{_examplesdir}/glide/tests
install sst1/glide/tests/tlib.[ch] $RPM_BUILD_ROOT%{_examplesdir}/glide/tests
gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/glide/tests/*.3df

# Install the texture tools source
install swlibs/texus/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/makefile
install swlibs/texus/lib/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/lib/makefile
install swlibs/texus/cmd/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/cmd/makefile
install swlibs/texus/examples/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/examples/makefile
install swlibs/texus/lib/*.c $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/lib
install swlibs/texus/lib/texusint.h $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/lib
install swlibs/texus/cmd/*.c $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/cmd
install swlibs/texus/examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/glide/texus/examples

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc glide_license.txt
%attr(755,root,root) %{_bindir}/texus
%attr(755,root,root) %{_bindir}/test3Dfx
%attr(755,root,root) %{_libdir}/libglide2x.so
%attr(755,root,root) %{_libdir}/libglide2x_VG.so
%attr(755,root,root) %{_libdir}/libtexus.so

%files -n Glide2x_SDK
%defattr(644,root,root,755)
%doc docs/*.pdf
%{_examplesdir}/glide
%{_includedir}/glide
