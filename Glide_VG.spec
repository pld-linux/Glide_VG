Summary:	Glide runtime for 3Dfx Voodoo Banshee and Voodoo3 boards
Name:		Glide_VG
Version:	2.46
Release:	4
Icon:		3dfx.gif
Source0:	Glide2.46.tar.gz
URL:		http://www.3dfx.com	
Copyright:	3DFX GLIDE Source Code General Public License
Vendor:		3Dfx Interactive Inc.
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows the user to use a 3dfx Interactive Voodoo Banshee
or Voodoo3 card under Linux.

%description -l pl
Dziêki tej bibliotece mozna uzywaæ kart Voodoo Banshee i Voodoo3 firmy
3dfx Interactive w systemie Linux.

%package -n Glide2x_SDK
Summary:	Development libraries for Glide 2.x
Version:	2.1
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description -n Glide2x_SDK
This package includes the headers files, documentation, and test files
necessary for developing applications that use the 3Dfx Interactive
Voodoo Graphics, Voodoo Rush, or Voodoo2 card.

%prep
%setup -q -c
chmod +x swlibs/include/make/ostype

%build

# No compatibility stuff if building for glibc2.0 directly
# First build for glibc20 using compatibility libraries
# export CC=i386-glibc20-linux-gcc
# make -f makefile.unix
# mv sst1/lib/libglide2x.so sst1/lib/libglide2x.glibc20
# mv swlibs/lib/libtexus.so swlibs/lib/libtexus.glibc20
# make -f makefile.unix clobber
# Now build for glibc2.1
# export CC=egcs
make -f makefile.unix

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_includedir}/glide
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/local/glide/bin
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/local/glide/src/tests
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/lib
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/cmd
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/examples
install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/doc/Glide2
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_includedir}
# install -d -m 755 $RPM_BUILD_ROOT%{_prefix}/i386-glibc20-linux/lib

# Install the glibc 2.1 libraries normally
install -m 755 sst1/lib/libglide2x.so $RPM_BUILD_ROOT%{_libdir}/libglide2x_VG.so
rm -f $RPM_BUILD_ROOT%{_libdir}/libglide2x.so
ln -s libglide2x_VG.so $RPM_BUILD_ROOT%{_libdir}/libglide2x.so
install -m 755 swlibs/lib/libtexus.so $RPM_BUILD_ROOT%{_libdir}

# Install the glibc 2.0 libraries in the compat directory
# install -m 755 sst1/lib/libglide2x.glibc20 $RPM_BUILD_ROOT%{_prefix}/i386-glibc20-linux/lib/libglide2x_VG.so
# rm -f $RPM_BUILD_ROOT%{_prefix}/i386-glibc20-linux/lib/libglide2x.so
# ln -s libglide2x_VG.so $RPM_BUILD_ROOT%{_prefix}/i386-glibc20-linux/lib/libglide2x.so
# install -m 755 swlibs/lib/libtexus.glibc20 $RPM_BUILD_ROOT%{_prefix}/i386-glibc20-linux/lib/libtexus.so

# Install the executables
install -m 755 swlibs/bin/texus $RPM_BUILD_ROOT%{_bindir}
# We don't ship these anymore because they are evil
# install -m 755 swlibs/bin/detect $RPM_BUILD_ROOT%{_prefix}/local/glide/bin
# install -m 755 swlibs/bin/pcirw $RPM_BUILD_ROOT%{_prefix}/local/glide/bin

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
install sst1/glide/tests/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/local/glide/src/tests/makefile
install -m 755 sst1/glide/tests/test00 $RPM_BUILD_ROOT%{_prefix}/local/glide/bin/test3Dfx
install sst1/glide/tests/*.3df $RPM_BUILD_ROOT%{_prefix}/local/glide/src/tests
install sst1/glide/tests/test??.c $RPM_BUILD_ROOT%{_prefix}/local/glide/src/tests
install sst1/glide/tests/tldata.inc $RPM_BUILD_ROOT%{_prefix}/local/glide/src/tests
install sst1/glide/tests/tlib.[ch] $RPM_BUILD_ROOT%{_prefix}/local/glide/src/tests

# Install the texture tools source
install swlibs/texus/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/makefile
install swlibs/texus/lib/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/lib/makefile
install swlibs/texus/cmd/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/cmd/makefile
install swlibs/texus/examples/makefile.distrib $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/examples/makefile
install swlibs/texus/lib/*.c $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/lib
install swlibs/texus/lib/texusint.h $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/lib
install swlibs/texus/cmd/*.c $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/cmd
install swlibs/texus/examples/*.c $RPM_BUILD_ROOT%{_prefix}/local/glide/src/texus/examples

# Install the documentation
install glide_license.txt $RPM_BUILD_ROOT%{_prefix}/doc/Glide2
install docs/*.pdf $RPM_BUILD_ROOT%{_prefix}/doc/Glide2

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

if [ "$1" = 1 ]; then
	# Cleanup old GlideSDK
	rm -rf /usr/local/glide/lib
	grep -v '/usr/local/glide/lib' /etc/ld.so.conf > /etc/ld.so.conf.tmp
	mv /etc/ld.so.conf.tmp /etc/ld.so.conf
fi

%post -n Glide2x_SDK

if [ "$1" = 1 ]; then
	# Cleanup old GlideSDK
	rm -rf /usr/local/glide/include
	set nonomatch
	rm -f /usr/local/glide/src/tldata.inc
	rm -f /usr/local/glide/src/Makefile
	rm -f /usr/local/glide/src/*.3df
	rm -f /usr/local/glide/src/*.c
	rm -f /usr/local/glide/src/*.h
fi

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%docdir %{_prefix}/doc/Glide2
%dir %{_prefix}/local/glide
%dir %{_prefix}/local/glide/bin
%{_prefix}/doc/Glide2/glide_license.txt
%{_libdir}/libglide2x.so
%{_libdir}/libglide2x_VG.so
%{_libdir}/libtexus.so
%attr(755,root,root) %{_bindir}/texus
%{_prefix}/local/glide/bin/test3Dfx
# %{_prefix}/i386-glibc20-linux/lib/libglide2x.so
# %{_prefix}/i386-glibc20-linux/lib/libglide2x_VG.so
# %{_prefix}/i386-glibc20-linux/lib/libtexus.so

%files -n Glide2x_SDK
%defattr(644,root,root,755)
%docdir %{_prefix}/doc/Glide2
%dir %{_prefix}/local/glide
%dir %{_prefix}/local/glide/bin
%{_prefix}/doc/Glide2/glidepgm.pdf
%{_prefix}/doc/Glide2/glideref.pdf
%{_prefix}/local/glide/src
# %{_prefix}/local/glide/bin/detect
# %{_prefix}/local/glide/bin/pcirw
%{_includedir}/glide
