#
# Conditional build:
%bcond_with	glide2_sdk	# build Glide2x_SDK here (normally built from Glide_V3.spec)
#
Summary:	Glide runtime for 3Dfx Voodoo Graphics boards
Summary(pl.UTF-8):	Środowisko Glide dla kart 3Dfx Voodoo Graphics
Name:		Glide_VG
Version:	2.46
Release:	11
License:	3DFX GLIDE Source Code General Public License
Group:		Libraries
Source0:	Glide%{version}.tar.gz
# Source0-md5:	be7762636b46cb04b238a16f45cfcfa8
Patch0:		%{name}-asm.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-morearchs.patch
Patch3:		%{name}-ioctl.patch
Patch4:		%{name}-soname.patch
Patch5:		%{name}-C_brainos.patch
Patch6:		%{name}-format.patch
Patch7:		%{name}-include.patch
URL:		http://glide.sourceforge.net/
%ifarch %{ix86}
BuildRequires:	/usr/bin/gasp
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows the user to use a 3Dfx Interactive Voodoo Graphics
card under Linux.

%description -l pl.UTF-8
Ten pakiet pozwala na używanie kart 3Dfx Interactive Voodoo Graphics
pod Linuksem.

%package devel
Summary:	Development package for Glide 2.x built for Voodoo Graphics
Summary(pl.UTF-8):	Pakiet programistyczny dla Glide 2.x zbudowanego dla Voodoo Graphics
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Glide2x_SDK >= %{version}
Provides:	Glide2x-devel = %{version}

%description devel
Development package for Glide 2.x built for 3Dfx Interactive Voodoo
Graphics adapters.

%description devel -l pl.UTF-8
Pakiet programistyczny dla Glide 2.x zbudowanego dla kart 3Dfx
Interactive Voodoo Graphics.

%package -n Glide2x_SDK
Summary:	Development files for Glide 2.x
Summary(pl.UTF-8):	Część Glide 2.x przeznaczona dla programistów
Group:		Development/Libraries
Conflicts:	Glide_SDK

%description -n Glide2x_SDK
This package includes the headers files, documentation, and test files
necessary for developing applications that use the 3Dfx Interactive
Voodoo Graphics, Voodoo Rush, or Voodoo2 card.

%description -n Glide2x_SDK -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe, dokumentację i pliki testowe
potrzebne do tworzenia aplikacji używających kart 3Dfx Interactive
Voodoo Graphics, Voodoo Rush lub Voodoo2.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
chmod +x swlibs/include/make/ostype

%build
%{__make} -j1 -f makefile.unix \
	AR="ar rcs" \
	CC="%{__cc}" \
	CNODEBUG="%{rpmcflags} -fPIC -Wno-missing-braces %{!?debug:-fomit-frame-pointer} \
	%{!?debug:-funroll-loops -fexpensive-optimizations -ffast-math}" \
%ifnarch %{ix86}
	FX_GLIDE_CTRISETUP=1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}

# Install the glibc 2.1 libraries normally
install sst1/lib/libglide.so.2.46 $RPM_BUILD_ROOT%{_libdir}
ln -sf libglide.so.2.46 $RPM_BUILD_ROOT%{_libdir}/libglide.so.2
ln -sf libglide.so.2 $RPM_BUILD_ROOT%{_libdir}/libglide2x.so
ln -sf libglide.so.2 $RPM_BUILD_ROOT%{_libdir}/libglide.so
install swlibs/lib/libtexus.so.1.1 $RPM_BUILD_ROOT%{_libdir}
ln -sf libtexus.so.1.1 $RPM_BUILD_ROOT%{_libdir}/libtexus.so.1
ln -sf libtexus.so.1 $RPM_BUILD_ROOT%{_libdir}/libtexus.so

# Install the executables
install swlibs/bin/texus $RPM_BUILD_ROOT%{_bindir}
install sst1/glide/tests/test00 $RPM_BUILD_ROOT%{_bindir}/test3Dfx

%if %{with glide2_sdk}
### SDK
install -d $RPM_BUILD_ROOT%{_includedir}/glide \
	$RPM_BUILD_ROOT%{_examplesdir}/glide2x-%{version}/{tests,texus/examples}

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
install sst1/glide/tests/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide2x-%{version}/tests/makefile
install sst1/glide/tests/*.3df $RPM_BUILD_ROOT%{_examplesdir}/glide2x-%{version}/tests
install sst1/glide/tests/test??.c $RPM_BUILD_ROOT%{_examplesdir}/glide2x-%{version}/tests
install sst1/glide/tests/tldata.inc $RPM_BUILD_ROOT%{_examplesdir}/glide2x-%{version}/tests
install sst1/glide/tests/tlib.[ch] $RPM_BUILD_ROOT%{_examplesdir}/glide2x-%{version}/tests
gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/glide2x-%{version}/tests/*.3df

# Install the texture tools source
install swlibs/texus/examples/makefile.distrib $RPM_BUILD_ROOT%{_examplesdir}/glide2x-%{version}/texus/examples/makefile
install swlibs/texus/examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/glide2x-%{version}/texus/examples
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc glide_license.txt readme.txt
%attr(755,root,root) %{_bindir}/texus
%attr(755,root,root) %{_bindir}/test3Dfx
%attr(755,root,root) %{_libdir}/libglide.so.2.46
%attr(755,root,root) %ghost %{_libdir}/libglide.so.2
%attr(755,root,root) %{_libdir}/libglide2x.so
%attr(755,root,root) %{_libdir}/libtexus.so.1.1
%attr(755,root,root) %ghost %{_libdir}/libtexus.so.1
%attr(755,root,root) %{_libdir}/libtexus.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglide.so

%if %{with glide2_sdk}
%files -n Glide2x_SDK
%defattr(644,root,root,755)
%doc docs/*.pdf
%{_includedir}/glide
%{_examplesdir}/glide2x-%{version}
%endif
