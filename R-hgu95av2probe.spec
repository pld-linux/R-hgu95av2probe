%define		packname	hgu95av2probe

Summary:	Probe sequence data for microarrays of type hgu95av2
Name:		R-%{packname}
Version:	2.13.0
Release:	1
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	eb4c614234b58f7e2a618b0f72f2d416
URL:		http://www.bioconductor.org/packages/release/data/annotation/html/hgu95av2probe.html
BuildRequires:	R-AnnotationDbi
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-AnnotationDbi
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package was automatically created by package matchprobes version
1.9.2. The probe sequence data was obtained from
http://www.affymetrix.com. The file name was HG\_U95Av2\_probe\_tab.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/NAMESPACE
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
