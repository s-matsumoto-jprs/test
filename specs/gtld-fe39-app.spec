# Conditional build
#

#
# rpmbuild -ba ~/rpm/SPECS/gtld-fe39-app.spec \
#              --define='version 20110804200913' \
#              --define='release PIW.019.REAL.REL'
#
%define fe1		f1
%define fe1basedir	/data/pasta0/
%define fe1appsdir	%{fe1basedir}/servlet/tomcat/webapps/

%define gtld_fe39_conf_app_ver       20210331214032
%define gtld_fe39_conf_tomcat_ver    20210331214032

%define debug_package %{nil}
%define __jar_repack %{nil}

%bcond_with branch

Summary:	gTLD Registrar System
Summary(ja):	gTLD Registrar System
Name:		gtld-fe39-app
Version:	%{version}
Release:	%{release}
License:	Copyright(c) 2018 JPRS
Group:		Applications/Internet/Registrar

%description
PASTA is a gTLD registrar system.

###
### gtld-app-whois-web
###
%package -n %{name}-whois-web-%{fe1}
Summary:	registrar whois web system
Group:		Applications/Internet/Registrar
Requires:	gtld-fe39-conf-app-%{fe1} >= %{gtld_fe39_conf_app_ver}
Requires:	gtld-fe39-conf-tomcat-%{fe1} >= %{gtld_fe39_conf_tomcat_ver}

%description -n %{name}-whois-web-%{fe1}
PASTA - whois web system

###
### gtld-app-whois-cmd
###
%package -n %{name}-whois-cmd-%{fe1}
Summary:	registrar whois command system
Group:		Applications/Internet/Registrar
Requires:	gtld-fe39-conf-app-%{fe1} >= %{gtld_fe39_conf_app_ver}

%description -n %{name}-whois-cmd-%{fe1}
PASTA - whois command system

###
### gtld-app-gtld-whois-cmd
###
%package -n %{name}-gtld-whois-cmd-%{fe1}
Summary:	gTLD whois command system
Group:		Applications/Internet/Registrar
Requires:	gtld-fe39-conf-app-%{fe1} >= %{gtld_fe39_conf_app_ver}

%description -n %{name}-gtld-whois-cmd-%{fe1}
PASTA - gTLD whois command system

###
### gtld-app-rdap
###
%package -n %{name}-rdap-%{fe1}
Summary:	registrar rdap system for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-fe39-conf-app-%{fe1} >= %{gtld_fe39_conf_app_ver}
Requires:	gtld-fe39-conf-tomcat-%{fe1} >= %{gtld_fe39_conf_tomcat_ver}

%description -n %{name}-rdap-%{fe1}
PASTA - rdap system

%prep
%setup -T -c %{name}-%{version}

%if %{with branch}
TAG=`echo %{release} | %__sed -e 's/\./-/g'`
if [ %{release} != "trunk" ]; then
    TAG="branches/${TAG}"
fi
%else
TAG="tags/"`echo %{release}-%{version} | %__sed -e 's/\./-/g'`
%endif
svn export http://svn1.jprs.co.jp/system/${TAG}/src


%build
export JAVA_HOME=/usr/local/jdk1.8/
cd ./src/domain/registrar
/usr/local/ant/bin/ant -f build.release.xml

%install
[ "${RPM_BUILD_ROOT}" != "/" ] && %__rm -rf ${RPM_BUILD_ROOT}

export JAR_BIN=/usr/local/jdk1.8/bin/jar

pushd ./src/domain/registrar/release

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-whois-web
%__install -p -m644 pasta-whois-web.war    ${RPM_BUILD_ROOT}/%{fe1appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-rdap
%__install -p -m644 pasta-rdap.war    ${RPM_BUILD_ROOT}/%{fe1appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/daemon/whois
%__install -p -m644 whoisd.zip       ${RPM_BUILD_ROOT}/%{fe1basedir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/daemon/gtld-whois
%__install -p -m644 gtld-whoisd.zip       ${RPM_BUILD_ROOT}/%{fe1basedir}

popd

pushd ./src/domain/registrar/config/gtd-real
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/whois-cmd
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/gtld-whois-cmd
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/whois-web
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/rdap
%__cp -pr whois-cmd ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr gtld-whois-cmd ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr whois-web ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr rdap ${RPM_BUILD_ROOT}/%{fe1basedir}/config
popd

pushd ./src/domain/registrar/htdocs/real
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/htdocs/pasta-whois-web
%__cp -pr pasta-whois-web ${RPM_BUILD_ROOT}/%{fe1basedir}/htdocs
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/htdocs/pasta-rdap
%__cp -pr pasta-rdap ${RPM_BUILD_ROOT}/%{fe1basedir}/htdocs
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/htdocs/pasta-www-rdap
%__cp -pr pasta-www-rdap ${RPM_BUILD_ROOT}/%{fe1basedir}/htdocs
popd


%pre -n %{name}-whois-web-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-whois-web/*

%pre -n %{name}-rdap-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-rdap/*

%pre -n %{name}-whois-cmd-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/whois/*

%pre -n %{name}-gtld-whois-cmd-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/gtld-whois/*

%preun -n %{name}-whois-web-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-whois-web/*
fi

%preun -n %{name}-rdap-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-rdap/*
fi

%preun -n %{name}-whois-cmd-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/whois/*
fi

%preun -n %{name}-gtld-whois-cmd-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/gtld-whois/*
fi


%post -n %{name}-whois-web-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-whois-web.war -d ./pasta-whois-web
%__chown -Rhf pasta0:pasta0 ./pasta-whois-web
popd

%post -n %{name}-rdap-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-rdap.war -d ./pasta-rdap
%__chown -Rhf pasta0:pasta0 ./pasta-rdap
popd

%post -n %{name}-whois-cmd-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}
%__unzip ./whoisd.zip -d ./daemon/whois
%__chmod 0755 ./daemon/whois/bin/*.sh
%__chown -Rhf pasta0:pasta0 ./daemon/whois
popd

%post -n %{name}-gtld-whois-cmd-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}
%__unzip ./gtld-whoisd.zip -d ./daemon/gtld-whois
%__chmod 0755 ./daemon/gtld-whois/bin/*.sh
%__chown -Rhf pasta0:pasta0 ./daemon/gtld-whois
popd

%clean
%__rm -rf ${RPM_BUILD_ROOT}

%files -n %{name}-whois-web-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/pasta-whois-web
%dir %{fe1basedir}/config/whois-web
%dir %{fe1basedir}/htdocs/pasta-whois-web
%{fe1appsdir}/pasta-whois-web.war
%{fe1basedir}/config/whois-web/log4j.xml
%{fe1basedir}/htdocs/pasta-whois-web/img
%{fe1basedir}/htdocs/pasta-whois-web/css
%{fe1basedir}/htdocs/pasta-whois-web/html
%{fe1basedir}/htdocs/pasta-whois-web/robots.txt

%files -n %{name}-rdap-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/pasta-rdap
%dir %{fe1basedir}/config/rdap
%dir %{fe1basedir}/htdocs/pasta-rdap
%dir %{fe1basedir}/htdocs/pasta-www-rdap
%dir %{fe1basedir}/htdocs/pasta-www-rdap/docs
%{fe1basedir}/htdocs/pasta-www-rdap/index.html
%{fe1appsdir}/pasta-rdap.war
%{fe1basedir}/config/rdap/log4j.xml

%files -n %{name}-whois-cmd-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1basedir}/daemon
%dir %{fe1basedir}/daemon/whois
%dir %{fe1basedir}/config/whois-cmd
%{fe1basedir}/whoisd.zip
%{fe1basedir}/config/whois-cmd/log4j.xml

%files -n %{name}-gtld-whois-cmd-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1basedir}/daemon
%dir %{fe1basedir}/daemon/gtld-whois
%dir %{fe1basedir}/config/gtld-whois-cmd
%{fe1basedir}/gtld-whoisd.zip
%{fe1basedir}/config/gtld-whois-cmd/log4j.xml


%changelog
* Tue Apr 6 2021 Yuki Matsuoka <y-matsuoka@jprs.co.jp>
- update: gtld_fe39_conf_app_ver       20210331214032
- update: gtld_fe39_conf_tomcat_ver    20210331214032

* Fri Sep 27 2019  Tsutomu Sakuma  <t-sakuma@jprs.co.jp>
- add: gtld-app-rdap htdocs files

* Wed Oct 24 2018  Satomi Yamashita  <s-yamashita@jprs.co.jp>
- add: gtld-app-rdap packages

* Fri Mar 23 2018 Kouji Takahashi <ko-takahashi@jprs.co.jp>
- update: gtld_fe39_conf_app_ver       20180323160709
- update: gtld_fe39_conf_tomcat_ver    20180323160709

* Tue Mar 20 2018 Kouji Takahashi <ko-takahashi@jprs.co.jp>
- add: debug_package
- add: __jar_repack

* Mon Jan 29 2018  Satomi Yamashita  <s-yamashita@jprs.co.jp>
- first release
