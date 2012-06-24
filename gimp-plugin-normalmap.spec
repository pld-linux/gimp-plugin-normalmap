Summary:	GIMP normalmap plugin
Summary(pl):	Mapa normalnych w GIMP-ie - wtyczka
Name:		gimp-plugin-normalmap
Version:	1.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://nifelheim.dyndns.org/~cocidius/files/gimp-normalmap-%{version}.tar.bz2
# Source0-md5:	d016b807098454d4fff3648d6feabddf
URL:		http://nifelheim.dyndns.org/~cocidius/normalmap/
BuildRequires:	gimp-devel >= 1:2.0.0
BuildRequires:	gtkglext-devel >= 0.7.1
BuildRequires:	pkgconfig >= 1:0.14
Obsoletes:	gimp-normalmap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
This is a plugin for GIMP versions 2.0.x. It allows you to convert
images into RGB normal maps for use in per-pixel lighting
applications. The goal is to completely clone NVIDIA's Photoshop
plugin, with a few new useful features.

Features:
- Filters. These include the filters found in the NVIDIA plugin (4
  sample, 3x3, 5x5, 7x7 and 9x9) with the addition of a 3x3 Sobel and
  Prewitt edge detection filter (yields the best results IMO).
- Post-filtering normal scaling
- Wrap mode. This allows the filters to wrap around the image. Useful
  for creating normalmaps from a tiling bumpmap.
- Height source. Use an average of the RGB components or the alpha
  channel as the height source in the generation of the normals.
- Alpha result. For RGBA images, the alpha channel can either remain
  unchanged, have the height used to generate the normal written to it,
  or be replaced by either 0 or 1.
- Conversion options including "Normalize only" for renormalizing
  bumpmaps.
- DU/DV map creation (8 and 16 bit, signed or unsigned)
- Dynamic 2D preview in the interactive dialog.
- Dynamic 3D preview window unsing OpenGL to view the normalmap
  applied to a lit primitive

%description -l pl
To jest wtyczka dla GIMP-a w wersji 2.0.x. Pozwala na konwersj�
obrazk�w na mapy RGB normalnych do u�ywania w aplikacjach
obliczaj�cych o�wietlenie na poziomie pikseli. Celem jest ca�kowite
sklonowanie wtyczki NVIDII do Photoshopa, z dodatkowymi przydatnymi
cechami.

Mo�liwo�ci:
- Filtry: obejmuj� filtry wyst�puj�ce we wtyczce NVIDII (4
  przyk�adowe: 3x3, 5x5, 7x7, 9x9) oraz dodatkowo filtr 3x3 Sobela i
  Prewitta z wykrywaniem kraw�dzi (daje najlepsze wyniki).
- Skalowanie normalnych w post-processingu.
- Tryb zawijania - pozwala filtrom na zawijanie wok� obrazu.
  Przydatne do tworzenia mapy normalnych z kaflowych map wysoko�ci.
- �r�d�o wysoko�ci. U�ycie �rednich sk�adowych RGB lub kana�u alpha
  jako �r�d�a wysoko�ci przy generowaniu normalnych.
- Wynik alpha. Dla obrazk�w RGBA kana� alpha mo�e pozosta�
  niezmieniony, by� wykorzystany jako wysoko�� przy generowaniu
  normalnych albo by� zast�piony przez 0 lub 1.
- Opcje konwersji w��cznie z sam� normalizacj� do renormalizacji map
  wysoko�ci.
- Tworzenie map DU/DV (8 i 16-bitowych, ze znakiem lub bez)
- Dynamiczny podgl�d 2D w interaktywnym oknie dialogowym.
- Dynamiczny podgl�d 3D w oddzielnym oknie z wykorzystaniem OpenGL do
  ogl�dania mapy normalnych na�o�onej na bry��.

%prep
%setup -q -n normalmap

%build
%{__make} \
	CFLAGS="%{rpmcflags} `gimptool --cflags` `pkg-config --cflags gtkglext-1.0` -DGETTEXT_PACKAGE" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install normalmap	$RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_plugindir}/*
