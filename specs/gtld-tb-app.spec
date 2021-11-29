# Conditional build
#

#
# rpmbuild -ba ~/rpm/SPECS/gtld-tb-app.spec \
#              --define='version 20110804200913' \
#              --define='release PIW.019.REAL.REL'
#
%define world           demo
%define fe1		f1
%define fe1basedir	/nfs/gtd/data/%{fe1}/pasta0/tb/
%define fe1appsdir	/nfs/gtd/data/%{fe1}/pasta0/servlet/tomcat/webapps/

%define fe2		f2
%define fe2basedir	/nfs/gtd/data/%{fe2}/pasta0/tb/
%define fe2appsdir	/nfs/gtd/data/%{fe2}/pasta0/servlet/tomcat/webapps/

%define privatedir	/nfs/gtd/share/private/system/pasta0/
%define publicdir	/nfs/gtd/share/public/system/pasta0/

%define agency_package     agency
%define agency_world       gtd-tb-%{agency_package}

%define gtld_conf_app_ver       20211124144253
%define gtld_conf_tomcat_ver    20211124144253



%define debug_package %{nil}
%define __jar_repack %{nil}

%bcond_with branch

Summary:	gTLD Registrar System (DEMO)
Summary(ja):	gTLD Registrar System (DEMO)
Name:		gtld-tb-app
Version:	%{version}
Release:	%{release}
License:	Copyright(c) 2010-2012,2021 JPRS
Group:		Applications/Internet/Registrar

%description
PASTA is a gTLD registrar system. (DEMO)

###
### gtld-tb-app-common
###
%package -n %{name}-common
Summary:	registrar transaction system common (DEMO)
Group:		Applications/Internet/Registrar
#Requires:	gtld-tb-conf-common >= %{gtld_conf_app_ver}

%description -n %{name}-common
PASTA - registrar jpp system common (DEMO)

###
### gtld-tb-app-agent-jpp
###
%package -n %{name}-agent-jpp-%{fe1}
Summary:	registrar transaction system for agents for f1 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-jpp-%{fe1}
PASTA - registrar jpp system for agents for f1 (DEMO)

%package -n %{name}-agent-jpp-%{fe2}
Summary:        registrar transaction system for agents for f2
Group:          Applications/Internet/Registrar (DEMO)
Requires:	gtld-tb-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-jpp-%{fe2}
PASTA - registrar jpp system for agents for f2 (DEMO)

###
### gtld-tb-app-agent-web
###
%package -n %{name}-agent-web-%{fe1}
Summary:	registrar web system for agents for f1 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-%{fe1}
PASTA - registrar web system for agents for f1 (DEMO)

%package -n %{name}-agent-web-%{fe2}
Summary:        registrar web system for agents for f2 (DEMO)
Group:          Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-%{fe2}
PASTA - registrar web system for agents for f2 (DEMO)

###
### gtld-tb-app-registrant-web
###
%package -n %{name}-registrant-web-%{fe1}
Summary:	registrar web system for registrants for f1 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-registrant-web-%{fe1}
PASTA - registrar web system for registrants for f1 (DEMO)

%package -n %{name}-registrant-web-%{fe2}
Summary:        registrar web system for registrants for f2 (DEMO)
Group:          Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-registrant-web-%{fe2}
PASTA - registrar web system for registrants for f2 (DEMO)

###
### gtld-tb-app-internal-web
###
%package -n %{name}-internal-web-%{fe1}
Summary:	registrar web system for employees for f1 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-internal-web-%{fe1}
PASTA - registrar web system for employees for f1 (DEMO)

%package -n %{name}-internal-web-%{fe2}
Summary:        registrar web system for employees for f2 (DEMO)
Group:          Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-internal-web-%{fe2}
PASTA - registrar web system for employees for f2 (DEMO)

###
### gtld-tb-app-resident
###
%package -n %{name}-resident-%{fe1}
Summary:	registrar resident system for f1 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-resident-%{fe1}
PASTA - registrar resident system for f1 (DEMO)

%package -n %{name}-resident-%{fe2}
Summary:        registrar resident system for f2 (DEMO)
Group:          Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-resident-%{fe2}
PASTA - registrar resident system for f2 (DEMO)

###
### gtld-tb-app-noresident
###
%package -n %{name}-noresident-%{fe1}
Summary:	registrar noresident system for f1 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-noresident-%{fe1}
PASTA - registrar noresident system for f1 (DEMO)

%package -n %{name}-noresident-%{fe2}
Summary:	registrar noresident system for f2 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-noresident-%{fe2}
PASTA - registrar noresident system for f2 (DEMO)

###
### gtld-tb-app-queue
###
%package -n %{name}-queue-%{fe1}
Summary:	registrar queue system for f1 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-queue-%{fe1}
PASTA - registrar queue system for f1 (DEMO)

%package -n %{name}-queue-%{fe2}
Summary:	registrar queue system for f2 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-queue-%{fe2}
PASTA - registrar queue system for f2 (DEMO)

###
### gtld-tb-app-scenario
###
%package -n %{name}-scenario-%{fe1}
Summary:	registrar scenario for f1 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-scenario-%{fe1}
PASTA - registrar scenario for f1 (DEMO)

%package -n %{name}-scenario-%{fe2}
Summary:	registrar scenario for f2 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-scenario-%{fe2}
PASTA - registrar scenario for f2 (DEMO)

###
### gtld-tb-app-agent-web-internal
###
%package -n %{name}-agent-web-internal-%{fe1}
Summary:	agent-web internal for f1 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-internal-%{fe1}
PASTA - agent-web internal for f1 (DEMO)

%package -n %{name}-agent-web-internal-%{fe2}
Summary:	agent-web internal for f2 (DEMO)
Group:		Applications/Internet/Registrar
Requires:	gtld-tb-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-internal-%{fe2}
PASTA - agent-web internal for f2 (DEMO)

###
### gtld-tb-app-agency
###
%package -n %{name}-%{agency_package}-%{fe1}
Summary:	registrar agency system for f1
Group:		Applications/Internet/Registrar

%description -n %{name}-%{agency_package}-%{fe1}
PASTA - gtd agency system for f1

%package -n %{name}-%{agency_package}-%{fe2}
Summary:	registrar agency system for f2
Group:		Applications/Internet/Registrar

%description -n %{name}-%{agency_package}-%{fe2}
PASTA - gtd agency system for f2

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
/usr/local/ant/bin/ant -f build.release.xml \
   -Drelease.mode=%{world}

%install
[ "${RPM_BUILD_ROOT}" != "/" ] && %__rm -rf ${RPM_BUILD_ROOT}

export JAR_BIN=/usr/local/jdk1.8/bin/jar

pushd ./src/domain/registrar/release

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-tb-agent-jpp
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/pasta-tb-agent-jpp
%__install -p -m644 pasta-tb-agent-jpp.war    ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 pasta-tb-agent-jpp.war    ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/gtd-tb-agent-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/gtd-tb-agent-web
%__install -p -m644 gtd-tb-agent-web.war      ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 gtd-tb-agent-web.war      ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-tb-internal-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/pasta-tb-internal-web
%__install -p -m644 pasta-tb-internal-web.war ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 pasta-tb-internal-web.war ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/gtd-tb-registrant-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/gtd-tb-registrant-web
%__install -p -m644 gtd-tb-registrant-web.war ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 gtd-tb-registrant-web.war ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-tb-resident-job
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/pasta-tb-resident-job
%__install -p -m644 pasta-tb-resident-job.war ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 pasta-tb-resident-job.war ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/standalone/job
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/standalone/job
%__install -p -m644 pasta-noresident.zip   ${RPM_BUILD_ROOT}/%{fe1basedir}
%__install -p -m644 pasta-noresident.zip   ${RPM_BUILD_ROOT}/%{fe2basedir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/daemon/job
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/daemon/job
%__install -p -m644 pasta-queue.zip        ${RPM_BUILD_ROOT}/%{fe1basedir}
%__install -p -m644 pasta-queue.zip        ${RPM_BUILD_ROOT}/%{fe2basedir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/scenario/job
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/scenario/job
%__install -p -m644 scenario.zip     ${RPM_BUILD_ROOT}/%{fe1basedir}
%__install -p -m644 scenario.zip     ${RPM_BUILD_ROOT}/%{fe2basedir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/gtd-tb-agent-web-internal
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/gtd-tb-agent-web-internal
%__install -p -m644 gtd-tb-agent-web-internal.war ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 gtd-tb-agent-web-internal.war ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/%{agency_world}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/%{agency_world}
%__install -p -m644 %{agency_world}.war      ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 %{agency_world}.war      ${RPM_BUILD_ROOT}/%{fe2appsdir}

popd

pushd ./src/domain/registrar/config/gtd-demo
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/agent-jpp
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/agent-web
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/agent-web-internal
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/internal-web
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/job
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/registrant-web
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/resident-job
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/agent-jpp
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/agent-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/agent-web-internal
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/internal-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/job
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/registrant-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/resident-job
%__cp -pr agent-jpp ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr agent-web ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr agent-web-internal ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr internal-web ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr job ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr registrant-web ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr resident-job ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr agent-jpp ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr agent-web ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr agent-web-internal ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr internal-web ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr job ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr registrant-web ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr resident-job ${RPM_BUILD_ROOT}/%{fe2basedir}/config
popd

pushd ./src/domain/registrar/htdocs
%__cp -pr demo ${RPM_BUILD_ROOT}/%{fe1basedir}/htdocs
%__cp -pr demo ${RPM_BUILD_ROOT}/%{fe2basedir}/htdocs
popd

%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/agent
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/bill
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/dns-err-del
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/dnsqc
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/dom-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/dom-trans
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/dom
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/expire
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/host
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/ns-set
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/ns
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/pub
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/recover-daily
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/recover-monthly
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/redirect
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/reg-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/reg-trans
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/reg
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/registrar-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/signingkey
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/upkeep-remind
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/pref-spool-apply
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/tb-lists/pref-spool-apply/tmp

%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/agent
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/bill
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/dns-err-del
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/dnsqc
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/dom-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/dom-trans
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/dom
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/expire
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/host
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/ns-set
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/ns
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/pub
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/recover-daily
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/recover-monthly
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/redirect
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/reg-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/reg-trans
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/reg
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/registrar-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/signingkey
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/tb-lists/upkeep-remind


%pre -n %{name}-agent-jpp-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-tb-agent-jpp/*

%pre -n %{name}-agent-jpp-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-tb-agent-jpp/*

%pre -n %{name}-agent-web-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-tb-agent-web/*

%pre -n %{name}-agent-web-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-tb-agent-web/*

%pre -n %{name}-internal-web-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-tb-internal-web/*

%pre -n %{name}-internal-web-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-tb-internal-web/*

%pre -n %{name}-registrant-web-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-tb-registrant-web/*

%pre -n %{name}-registrant-web-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-tb-registrant-web/*

%pre -n %{name}-resident-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-tb-resident-job/*

%pre -n %{name}-resident-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-tb-resident-job/*

%pre -n %{name}-agent-web-internal-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-tb-agent-web-internal/*

%pre -n %{name}-agent-web-internal-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-tb-agent-web-internal/*

%pre -n %{name}-noresident-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/standalone/job/*

%pre -n %{name}-noresident-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/standalone/job/*

%pre -n %{name}-queue-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/job/*

%pre -n %{name}-queue-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/daemon/job/*

%pre -n %{name}-scenario-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/scenario/job/*

%pre -n %{name}-scenario-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/scenario/job/*

%pre -n %{name}-%{agency_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{agency_world}/*

%pre -n %{name}-%{agency_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{agency_world}/*

%preun -n %{name}-agent-jpp-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-tb-agent-jpp/*
fi

%preun -n %{name}-agent-jpp-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-tb-agent-jpp/*
fi

%preun -n %{name}-agent-web-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-tb-agent-web/*
fi

%preun -n %{name}-agent-web-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-tb-agent-web/*
fi

%preun -n %{name}-internal-web-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-tb-internal-web/*
fi

%preun -n %{name}-internal-web-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-tb-internal-web/*
fi

%preun -n %{name}-registrant-web-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-tb-registrant-web/*
fi

%preun -n %{name}-registrant-web-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-tb-registrant-web/*
fi

%preun -n %{name}-resident-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-tb-resident-job/*
fi

%preun -n %{name}-resident-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-tb-resident-job/*
fi

%preun -n %{name}-agent-web-internal-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-tb-agent-web-internal/*
fi

%preun -n %{name}-agent-web-internal-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-tb-agent-web-internal/*
fi

%preun -n %{name}-noresident-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/standalone/job/*
fi

%preun -n %{name}-noresident-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/standalone/job/*
fi

%preun -n %{name}-queue-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/job/*
fi

%preun -n %{name}-queue-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/daemon/job/*
fi

%preun -n %{name}-scenario-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/scenario/job/*
fi

%preun -n %{name}-scenario-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/scenario/job/*
fi

%preun -n %{name}-%{agency_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{agency_world}/*
fi

%preun -n %{name}-%{agency_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{agency_world}/*
fi


%post -n %{name}-agent-jpp-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-tb-agent-jpp.war -d ./pasta-tb-agent-jpp
%__chown -Rhf pasta0:pasta0 ./pasta-tb-agent-jpp
popd

%post -n %{name}-agent-jpp-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./pasta-tb-agent-jpp.war -d ./pasta-tb-agent-jpp
%__chown -Rhf pasta0:pasta0 ./pasta-tb-agent-jpp
popd

%post -n %{name}-agent-web-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./gtd-tb-agent-web.war -d ./gtd-tb-agent-web
%__chown -Rhf pasta0:pasta0 ./gtd-tb-agent-web
popd

%post -n %{name}-agent-web-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./gtd-tb-agent-web.war -d ./gtd-tb-agent-web
%__chown -Rhf pasta0:pasta0 ./gtd-tb-agent-web
popd

%post -n %{name}-internal-web-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-tb-internal-web.war -d ./pasta-tb-internal-web
%__chown -Rhf pasta0:pasta0 ./pasta-tb-internal-web
popd

%post -n %{name}-internal-web-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./pasta-tb-internal-web.war -d ./pasta-tb-internal-web
%__chown -Rhf pasta0:pasta0 ./pasta-tb-internal-web
popd

%post -n %{name}-registrant-web-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./gtd-tb-registrant-web.war -d ./gtd-tb-registrant-web
%__chown -Rhf pasta0:pasta0 ./gtd-tb-registrant-web
popd

%post -n %{name}-registrant-web-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./gtd-tb-registrant-web.war -d ./gtd-tb-registrant-web
%__chown -Rhf pasta0:pasta0 ./gtd-tb-registrant-web
popd

%post -n %{name}-resident-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-tb-resident-job.war -d ./pasta-tb-resident-job
%__chown -Rhf pasta0:pasta0 ./pasta-tb-resident-job
popd

%post -n %{name}-resident-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./pasta-tb-resident-job.war -d ./pasta-tb-resident-job
%__chown -Rhf pasta0:pasta0 ./pasta-tb-resident-job
popd

%post -n %{name}-agent-web-internal-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./gtd-tb-agent-web-internal.war -d ./gtd-tb-agent-web-internal
%__chown -Rhf pasta0:pasta0 ./gtd-tb-agent-web-internal
popd

%post -n %{name}-agent-web-internal-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./gtd-tb-agent-web-internal.war -d ./gtd-tb-agent-web-internal
%__chown -Rhf pasta0:pasta0 ./gtd-tb-agent-web-internal
popd

%post -n %{name}-noresident-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}
%__unzip ./pasta-noresident.zip -d ./standalone/job
%__chown -Rhf pasta0:pasta0 ./standalone/job
popd

%post -n %{name}-noresident-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}
%__unzip ./pasta-noresident.zip -d ./standalone/job
%__chown -Rhf pasta0:pasta0 ./standalone/job
popd

%post -n %{name}-queue-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}
%__unzip ./pasta-queue.zip -d ./daemon/job
%__chown -Rhf pasta0:pasta0 ./daemon/job
popd

%post -n %{name}-queue-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}
%__unzip ./pasta-queue.zip -d ./daemon/job
%__chown -Rhf pasta0:pasta0 ./daemon/job
popd

%post -n %{name}-scenario-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}
%__unzip ./scenario.zip -d ./scenario/job
%__chmod 0755 ./scenario/job/*.sh
%__chmod 0755 ./scenario/job/tools/*
%__chmod 0755 ./scenario/job/sbin/*
%__chmod 0755 ./scenario/job/dr/bin/*.sh
%__chown -Rhf pasta0:pasta0 ./scenario/job
popd

%post -n %{name}-scenario-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}
%__unzip ./scenario.zip -d ./scenario/job
%__chmod 0755 ./scenario/job/*.sh
%__chmod 0755 ./scenario/job/tools/*
%__chmod 0755 ./scenario/job/sbin/*
%__chmod 0755 ./scenario/job/dr/bin/*.sh
%__chown -Rhf pasta0:pasta0 ./scenario/job
popd

%post -n %{name}-%{agency_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./%{agency_world}.war -d ./%{agency_world}
%__chown -Rhf pasta0:pasta0 ./%{agency_world}
popd

%post -n %{name}-%{agency_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./%{agency_world}.war -d ./%{agency_world}
%__chown -Rhf pasta0:pasta0 ./%{agency_world}
popd

%clean
%__rm -rf ${RPM_BUILD_ROOT}

%files -n %{name}-common
%defattr(-,pasta0,pasta0)
%dir %{privatedir}/tb-lists
%dir %{privatedir}/tb-lists/agent
%dir %{privatedir}/tb-lists/bill
%dir %{privatedir}/tb-lists/dns-err-del
%dir %{privatedir}/tb-lists/dnsqc
%dir %{privatedir}/tb-lists/dom-trans-apply
%dir %{privatedir}/tb-lists/dom-trans
%dir %{privatedir}/tb-lists/dom
%dir %{privatedir}/tb-lists/expire
%dir %{privatedir}/tb-lists/host
%dir %{privatedir}/tb-lists/ns-set
%dir %{privatedir}/tb-lists/ns
%dir %{privatedir}/tb-lists/pub
%dir %{privatedir}/tb-lists/recover-daily
%dir %{privatedir}/tb-lists/recover-monthly
%dir %{privatedir}/tb-lists/redirect
%dir %{privatedir}/tb-lists/reg-trans-apply
%dir %{privatedir}/tb-lists/reg-trans
%dir %{privatedir}/tb-lists/reg
%dir %{privatedir}/tb-lists/registrar-trans-apply
%dir %{privatedir}/tb-lists/signingkey
%dir %{privatedir}/tb-lists/upkeep-remind
%dir %{privatedir}/tb-lists/pref-spool-apply
%dir %{privatedir}/tb-lists/pref-spool-apply/tmp
%dir %{publicdir}/tb-lists
%dir %{publicdir}/tb-lists/agent
%dir %{publicdir}/tb-lists/bill
%dir %{publicdir}/tb-lists/dns-err-del
%dir %{publicdir}/tb-lists/dnsqc
%dir %{publicdir}/tb-lists/dom-trans-apply
%dir %{publicdir}/tb-lists/dom-trans
%dir %{publicdir}/tb-lists/dom
%dir %{publicdir}/tb-lists/expire
%dir %{publicdir}/tb-lists/host
%dir %{publicdir}/tb-lists/ns-set
%dir %{publicdir}/tb-lists/ns
%dir %{publicdir}/tb-lists/pub
%dir %{publicdir}/tb-lists/recover-daily
%dir %{publicdir}/tb-lists/recover-monthly
%dir %{publicdir}/tb-lists/redirect
%dir %{publicdir}/tb-lists/reg-trans-apply
%dir %{publicdir}/tb-lists/reg-trans
%dir %{publicdir}/tb-lists/reg
%dir %{publicdir}/tb-lists/registrar-trans-apply
%dir %{publicdir}/tb-lists/signingkey
%dir %{publicdir}/tb-lists/upkeep-remind


%files -n %{name}-agent-jpp-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/pasta-tb-agent-jpp
%dir %{fe1basedir}
%dir %{fe1basedir}/config
%dir %{fe1basedir}/config/agent-jpp
%dir %{fe1basedir}/config/agent-jpp/afilias
%dir %{fe1basedir}/config/agent-jpp/ari
%dir %{fe1basedir}/config/agent-jpp/gmo
%dir %{fe1basedir}/config/agent-jpp/neustar
%dir %{fe1basedir}/config/agent-jpp/verisign
%{fe1appsdir}/pasta-tb-agent-jpp.war
%{fe1basedir}/config/agent-jpp/afilias/rtk.properties
%{fe1basedir}/config/agent-jpp/ari/logconfig.xml
%{fe1basedir}/config/agent-jpp/gmo/rtk.properties
%{fe1basedir}/config/agent-jpp/neustar/logconfig.xml
%{fe1basedir}/config/agent-jpp/verisign/logconfig.xml
%{fe1basedir}/config/agent-jpp/gjp_transaction.xml
%{fe1basedir}/config/agent-jpp/log4j.xml

%files -n %{name}-agent-jpp-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/pasta-tb-agent-jpp
%dir %{fe2basedir}
%dir %{fe2basedir}/config
%dir %{fe2basedir}/config/agent-jpp
%dir %{fe2basedir}/config/agent-jpp/afilias
%dir %{fe2basedir}/config/agent-jpp/ari
%dir %{fe2basedir}/config/agent-jpp/gmo
%dir %{fe2basedir}/config/agent-jpp/neustar
%dir %{fe2basedir}/config/agent-jpp/verisign
%{fe2appsdir}/pasta-tb-agent-jpp.war
%{fe2basedir}/config/agent-jpp/afilias/rtk.properties
%{fe2basedir}/config/agent-jpp/ari/logconfig.xml
%{fe2basedir}/config/agent-jpp/gmo/rtk.properties
%{fe2basedir}/config/agent-jpp/neustar/logconfig.xml
%{fe2basedir}/config/agent-jpp/verisign/logconfig.xml
%{fe2basedir}/config/agent-jpp/gjp_transaction.xml
%{fe2basedir}/config/agent-jpp/log4j.xml


%files -n %{name}-agent-web-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/gtd-tb-agent-web
%dir %{fe1basedir}/config/agent-web
%dir %{fe1basedir}/config/agent-web/afilias
%dir %{fe1basedir}/config/agent-web/ari
%dir %{fe1basedir}/config/agent-web/gmo
%dir %{fe1basedir}/config/agent-web/neustar
%dir %{fe1basedir}/config/agent-web/verisign
%dir %{fe1basedir}/htdocs
%dir %{fe1basedir}/htdocs/gtd-agent-web
%dir %{fe1basedir}/htdocs/gtd-agent-web/gtd-agent-web
%{fe1appsdir}/gtd-tb-agent-web.war
%{fe1basedir}/config/agent-web/afilias/rtk.properties
%{fe1basedir}/config/agent-web/ari/logconfig.xml
%{fe1basedir}/config/agent-web/gmo/rtk.properties
%{fe1basedir}/config/agent-web/neustar/logconfig.xml
%{fe1basedir}/config/agent-web/verisign/logconfig.xml
%{fe1basedir}/config/agent-web/gjp_transaction.xml
%{fe1basedir}/config/agent-web/log4j.xml
%{fe1basedir}/htdocs/gtd-agent-web/img
%{fe1basedir}/htdocs/gtd-agent-web/gtd-agent-web/img

%files -n %{name}-agent-web-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/gtd-tb-agent-web
%dir %{fe2basedir}/config/agent-web
%dir %{fe2basedir}/config/agent-web/afilias
%dir %{fe2basedir}/config/agent-web/ari
%dir %{fe2basedir}/config/agent-web/gmo
%dir %{fe2basedir}/config/agent-web/neustar
%dir %{fe2basedir}/config/agent-web/verisign
%dir %{fe2basedir}/htdocs
%dir %{fe2basedir}/htdocs/gtd-agent-web
%dir %{fe2basedir}/htdocs/gtd-agent-web/gtd-agent-web
%{fe2appsdir}/gtd-tb-agent-web.war
%{fe2basedir}/config/agent-web/afilias/rtk.properties
%{fe2basedir}/config/agent-web/ari/logconfig.xml
%{fe2basedir}/config/agent-web/gmo/rtk.properties
%{fe2basedir}/config/agent-web/neustar/logconfig.xml
%{fe2basedir}/config/agent-web/verisign/logconfig.xml
%{fe2basedir}/config/agent-web/gjp_transaction.xml
%{fe2basedir}/config/agent-web/log4j.xml
%{fe2basedir}/htdocs/gtd-agent-web/img
%{fe2basedir}/htdocs/gtd-agent-web/gtd-agent-web/img


%files -n %{name}-internal-web-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/pasta-tb-internal-web
%dir %{fe1basedir}/config/internal-web
%dir %{fe1basedir}/htdocs/pasta-internal-web
%dir %{fe1basedir}/htdocs/pasta-internal-web/pasta-internal-web
%{fe1appsdir}/pasta-tb-internal-web.war
%{fe1basedir}/config/internal-web/gjp_transaction.xml
%{fe1basedir}/config/internal-web/log4j.xml
%{fe1basedir}/htdocs/pasta-internal-web/img
%{fe1basedir}/htdocs/pasta-internal-web/pasta-internal-web/img

%files -n %{name}-internal-web-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/pasta-tb-internal-web
%dir %{fe2basedir}/config/internal-web
%dir %{fe2basedir}/htdocs/pasta-internal-web
%dir %{fe2basedir}/htdocs/pasta-internal-web/pasta-internal-web
%{fe2appsdir}/pasta-tb-internal-web.war
%{fe2basedir}/config/internal-web/gjp_transaction.xml
%{fe2basedir}/config/internal-web/log4j.xml
%{fe2basedir}/htdocs/pasta-internal-web/img
%{fe2basedir}/htdocs/pasta-internal-web/pasta-internal-web/img


%files -n %{name}-registrant-web-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/gtd-tb-registrant-web
%dir %{fe1basedir}/config/registrant-web
%dir %{fe1basedir}/config/registrant-web/afilias
%dir %{fe1basedir}/config/registrant-web/ari
%dir %{fe1basedir}/config/registrant-web/gmo
%dir %{fe1basedir}/config/registrant-web/neustar
%dir %{fe1basedir}/config/registrant-web/verisign
%dir %{fe1basedir}/htdocs/gtd-registrant-web
%dir %{fe1basedir}/htdocs/gtd-registrant-web/gtd-registrant-web
%dir %{fe1basedir}/htdocs/gtd-agent-web/gtd-registrant-web
%{fe1appsdir}/gtd-tb-registrant-web.war
%{fe1basedir}/config/registrant-web/afilias/rtk.properties
%{fe1basedir}/config/registrant-web/ari/logconfig.xml
%{fe1basedir}/config/registrant-web/gmo/rtk.properties
%{fe1basedir}/config/registrant-web/neustar/logconfig.xml
%{fe1basedir}/config/registrant-web/verisign/logconfig.xml
%{fe1basedir}/config/registrant-web/gjp_transaction.xml
%{fe1basedir}/config/registrant-web/log4j.xml
%{fe1basedir}/htdocs/gtd-registrant-web/img
%{fe1basedir}/htdocs/gtd-registrant-web/gtd-registrant-web/img
%{fe1basedir}/htdocs/gtd-agent-web/gtd-registrant-web/img

%files -n %{name}-registrant-web-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/gtd-tb-registrant-web
%dir %{fe2basedir}/config/registrant-web
%dir %{fe2basedir}/config/registrant-web/afilias
%dir %{fe2basedir}/config/registrant-web/ari
%dir %{fe2basedir}/config/registrant-web/gmo
%dir %{fe2basedir}/config/registrant-web/neustar
%dir %{fe2basedir}/config/registrant-web/verisign
%dir %{fe2basedir}/htdocs/gtd-registrant-web
%dir %{fe2basedir}/htdocs/gtd-registrant-web/gtd-registrant-web
%dir %{fe2basedir}/htdocs/gtd-agent-web/gtd-registrant-web
%{fe2appsdir}/gtd-tb-registrant-web.war
%{fe2basedir}/config/registrant-web/afilias/rtk.properties
%{fe2basedir}/config/registrant-web/ari/logconfig.xml
%{fe2basedir}/config/registrant-web/gmo/rtk.properties
%{fe2basedir}/config/registrant-web/neustar/logconfig.xml
%{fe2basedir}/config/registrant-web/verisign/logconfig.xml
%{fe2basedir}/config/registrant-web/gjp_transaction.xml
%{fe2basedir}/config/registrant-web/log4j.xml
%{fe2basedir}/htdocs/gtd-registrant-web/img
%{fe2basedir}/htdocs/gtd-registrant-web/gtd-registrant-web/img
%{fe2basedir}/htdocs/gtd-agent-web/gtd-registrant-web/img


%files -n %{name}-resident-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/pasta-tb-resident-job
%dir %{fe1basedir}/config/resident-job
%dir %{fe1basedir}/config/resident-job/afilias
%dir %{fe1basedir}/config/resident-job/ari
%dir %{fe1basedir}/config/resident-job/gmo
%dir %{fe1basedir}/config/resident-job/neustar
%dir %{fe1basedir}/config/resident-job/verisign
%{fe1appsdir}/pasta-tb-resident-job.war
%{fe1basedir}/config/resident-job/afilias/rtk.properties
%{fe1basedir}/config/resident-job/ari/logconfig.xml
%{fe1basedir}/config/resident-job/gmo/rtk.properties
%{fe1basedir}/config/resident-job/neustar/logconfig.xml
%{fe1basedir}/config/resident-job/verisign/logconfig.xml
%{fe1basedir}/config/resident-job/log4j.xml

%files -n %{name}-resident-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/pasta-tb-resident-job
%dir %{fe2basedir}/config/resident-job
%dir %{fe2basedir}/config/resident-job/afilias
%dir %{fe2basedir}/config/resident-job/ari
%dir %{fe2basedir}/config/resident-job/gmo
%dir %{fe2basedir}/config/resident-job/neustar
%dir %{fe2basedir}/config/resident-job/verisign
%{fe2appsdir}/pasta-tb-resident-job.war
%{fe2basedir}/config/resident-job/afilias/rtk.properties
%{fe2basedir}/config/resident-job/ari/logconfig.xml
%{fe2basedir}/config/resident-job/gmo/rtk.properties
%{fe2basedir}/config/resident-job/neustar/logconfig.xml
%{fe2basedir}/config/resident-job/verisign/logconfig.xml
%{fe2basedir}/config/resident-job/log4j.xml


%files -n %{name}-agent-web-internal-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/gtd-tb-agent-web-internal
%dir %{fe1basedir}/config/agent-web-internal
%dir %{fe1basedir}/config/agent-web-internal/afilias
%dir %{fe1basedir}/config/agent-web-internal/ari
%dir %{fe1basedir}/config/agent-web-internal/gmo
%dir %{fe1basedir}/config/agent-web-internal/neustar
%dir %{fe1basedir}/config/agent-web-internal/verisign
%dir %{fe1basedir}/htdocs/gtd-agent-web-internal
%dir %{fe1basedir}/htdocs/gtd-agent-web-internal/gtd-agent-web-internal
%{fe1appsdir}/gtd-tb-agent-web-internal.war
%{fe1basedir}/config/agent-web-internal/afilias/rtk.properties
%{fe1basedir}/config/agent-web-internal/ari/logconfig.xml
%{fe1basedir}/config/agent-web-internal/gmo/rtk.properties
%{fe1basedir}/config/agent-web-internal/neustar/logconfig.xml
%{fe1basedir}/config/agent-web-internal/verisign/logconfig.xml
%{fe1basedir}/config/agent-web-internal/gjp_transaction.xml
%{fe1basedir}/config/agent-web-internal/log4j.xml
%{fe1basedir}/htdocs/gtd-agent-web-internal/img
%{fe1basedir}/htdocs/gtd-agent-web-internal/gtd-agent-web-internal/img

%files -n %{name}-agent-web-internal-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/gtd-tb-agent-web-internal
%dir %{fe2basedir}/config/agent-web-internal
%dir %{fe2basedir}/config/agent-web-internal/afilias
%dir %{fe2basedir}/config/agent-web-internal/ari
%dir %{fe2basedir}/config/agent-web-internal/gmo
%dir %{fe2basedir}/config/agent-web-internal/neustar
%dir %{fe2basedir}/config/agent-web-internal/verisign
%dir %{fe2basedir}/htdocs/gtd-agent-web-internal
%dir %{fe2basedir}/htdocs/gtd-agent-web-internal/gtd-agent-web-internal
%{fe2appsdir}/gtd-tb-agent-web-internal.war
%{fe2basedir}/config/agent-web-internal/afilias/rtk.properties
%{fe2basedir}/config/agent-web-internal/ari/logconfig.xml
%{fe2basedir}/config/agent-web-internal/gmo/rtk.properties
%{fe2basedir}/config/agent-web-internal/neustar/logconfig.xml
%{fe2basedir}/config/agent-web-internal/verisign/logconfig.xml
%{fe2basedir}/config/agent-web-internal/gjp_transaction.xml
%{fe2basedir}/config/agent-web-internal/log4j.xml
%{fe2basedir}/htdocs/gtd-agent-web-internal/img
%{fe2basedir}/htdocs/gtd-agent-web-internal/gtd-agent-web-internal/img


%files -n %{name}-noresident-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1basedir}/standalone
%dir %{fe1basedir}/standalone/job
%{fe1basedir}/pasta-noresident.zip

%files -n %{name}-noresident-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2basedir}/standalone
%dir %{fe2basedir}/standalone/job
%{fe2basedir}/pasta-noresident.zip


%files -n %{name}-queue-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1basedir}/daemon
%dir %{fe1basedir}/daemon/job
%{fe1basedir}/pasta-queue.zip

%files -n %{name}-queue-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2basedir}/daemon
%dir %{fe2basedir}/daemon/job
%{fe2basedir}/pasta-queue.zip


%files -n %{name}-scenario-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1basedir}/scenario
%dir %{fe1basedir}/scenario/job
%dir %{fe1basedir}/config/job
%dir %{fe1basedir}/config/job/apl002
%dir %{fe1basedir}/config/job/apl002/afilias
%dir %{fe1basedir}/config/job/apl002/ari
%dir %{fe1basedir}/config/job/apl002/gmo
%dir %{fe1basedir}/config/job/apl002/neustar
%dir %{fe1basedir}/config/job/apl002/verisign
%dir %{fe1basedir}/config/job/apl009
%dir %{fe1basedir}/config/job/apl009/afilias
%dir %{fe1basedir}/config/job/apl009/ari
%dir %{fe1basedir}/config/job/apl009/gmo
%dir %{fe1basedir}/config/job/apl009/neustar
%dir %{fe1basedir}/config/job/apl009/verisign
%dir %{fe1basedir}/config/job/apl010
%dir %{fe1basedir}/config/job/apl010/afilias
%dir %{fe1basedir}/config/job/apl010/ari
%dir %{fe1basedir}/config/job/apl010/gmo
%dir %{fe1basedir}/config/job/apl010/neustar
%dir %{fe1basedir}/config/job/apl010/verisign
%dir %{fe1basedir}/config/job/apl036
%dir %{fe1basedir}/config/job/apl036/afilias
%dir %{fe1basedir}/config/job/apl036/ari
%dir %{fe1basedir}/config/job/apl036/gmo
%dir %{fe1basedir}/config/job/apl036/neustar
%dir %{fe1basedir}/config/job/apl036/verisign
%dir %{fe1basedir}/config/job/apl066
%dir %{fe1basedir}/config/job/apl066/afilias
%dir %{fe1basedir}/config/job/apl066/ari
%dir %{fe1basedir}/config/job/apl066/gmo
%dir %{fe1basedir}/config/job/apl066/neustar
%dir %{fe1basedir}/config/job/apl066/verisign
%dir %{fe1basedir}/config/job/apl083
%dir %{fe1basedir}/config/job/apl083/afilias
%dir %{fe1basedir}/config/job/apl083/ari
%dir %{fe1basedir}/config/job/apl083/gmo
%dir %{fe1basedir}/config/job/apl083/neustar
%dir %{fe1basedir}/config/job/apl083/verisign
%dir %{fe1basedir}/config/job/apl087
%dir %{fe1basedir}/config/job/apl087/afilias
%dir %{fe1basedir}/config/job/apl087/ari
%dir %{fe1basedir}/config/job/apl087/gmo
%dir %{fe1basedir}/config/job/apl087/neustar
%dir %{fe1basedir}/config/job/apl087/verisign
%dir %{fe1basedir}/config/job/mon001
%dir %{fe1basedir}/config/job/mon001/afilias
%dir %{fe1basedir}/config/job/mon001/ari
%dir %{fe1basedir}/config/job/mon001/gmo
%dir %{fe1basedir}/config/job/mon001/neustar
%dir %{fe1basedir}/config/job/mon001/verisign
%{fe1basedir}/scenario.zip
%{fe1basedir}/config/job/apl002/afilias/rtk.properties
%{fe1basedir}/config/job/apl002/ari/logconfig.xml
%{fe1basedir}/config/job/apl002/gmo/rtk.properties
%{fe1basedir}/config/job/apl002/neustar/logconfig.xml
%{fe1basedir}/config/job/apl002/verisign/logconfig.xml
%{fe1basedir}/config/job/apl009/afilias/rtk.properties
%{fe1basedir}/config/job/apl009/ari/logconfig.xml
%{fe1basedir}/config/job/apl009/gmo/rtk.properties
%{fe1basedir}/config/job/apl009/neustar/logconfig.xml
%{fe1basedir}/config/job/apl009/verisign/logconfig.xml
%{fe1basedir}/config/job/apl010/afilias/rtk.properties
%{fe1basedir}/config/job/apl010/ari/logconfig.xml
%{fe1basedir}/config/job/apl010/gmo/rtk.properties
%{fe1basedir}/config/job/apl010/neustar/logconfig.xml
%{fe1basedir}/config/job/apl010/verisign/logconfig.xml
%{fe1basedir}/config/job/apl036/afilias/rtk.properties
%{fe1basedir}/config/job/apl036/ari/logconfig.xml
%{fe1basedir}/config/job/apl036/gmo/rtk.properties
%{fe1basedir}/config/job/apl036/neustar/logconfig.xml
%{fe1basedir}/config/job/apl036/verisign/logconfig.xml
%{fe1basedir}/config/job/apl066/afilias/rtk.properties
%{fe1basedir}/config/job/apl066/ari/logconfig.xml
%{fe1basedir}/config/job/apl066/gmo/rtk.properties
%{fe1basedir}/config/job/apl066/neustar/logconfig.xml
%{fe1basedir}/config/job/apl066/verisign/logconfig.xml
%{fe1basedir}/config/job/apl083/afilias/rtk.properties
%{fe1basedir}/config/job/apl083/ari/logconfig.xml
%{fe1basedir}/config/job/apl083/gmo/rtk.properties
%{fe1basedir}/config/job/apl083/neustar/logconfig.xml
%{fe1basedir}/config/job/apl083/verisign/logconfig.xml
%{fe1basedir}/config/job/apl087/afilias/rtk.properties
%{fe1basedir}/config/job/apl087/ari/logconfig.xml
%{fe1basedir}/config/job/apl087/gmo/rtk.properties
%{fe1basedir}/config/job/apl087/neustar/logconfig.xml
%{fe1basedir}/config/job/apl087/verisign/logconfig.xml
%{fe1basedir}/config/job/mon001/afilias/rtk.properties
%{fe1basedir}/config/job/mon001/ari/logconfig.xml
%{fe1basedir}/config/job/mon001/gmo/rtk.properties
%{fe1basedir}/config/job/mon001/neustar/logconfig.xml
%{fe1basedir}/config/job/mon001/verisign/logconfig.xml
%{fe1basedir}/config/job/gjp_transaction.xml
%{fe1basedir}/config/job/job_*_log4j.xml

%files -n %{name}-scenario-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2basedir}/scenario
%dir %{fe2basedir}/scenario/job
%dir %{fe2basedir}/config/job
%dir %{fe2basedir}/config/job/apl002
%dir %{fe2basedir}/config/job/apl002/afilias
%dir %{fe2basedir}/config/job/apl002/ari
%dir %{fe2basedir}/config/job/apl002/gmo
%dir %{fe2basedir}/config/job/apl002/neustar
%dir %{fe2basedir}/config/job/apl002/verisign
%dir %{fe2basedir}/config/job/apl009
%dir %{fe2basedir}/config/job/apl009/afilias
%dir %{fe2basedir}/config/job/apl009/ari
%dir %{fe2basedir}/config/job/apl009/gmo
%dir %{fe2basedir}/config/job/apl009/neustar
%dir %{fe2basedir}/config/job/apl009/verisign
%dir %{fe2basedir}/config/job/apl010
%dir %{fe2basedir}/config/job/apl010/afilias
%dir %{fe2basedir}/config/job/apl010/ari
%dir %{fe2basedir}/config/job/apl010/gmo
%dir %{fe2basedir}/config/job/apl010/neustar
%dir %{fe2basedir}/config/job/apl010/verisign
%dir %{fe2basedir}/config/job/apl036
%dir %{fe2basedir}/config/job/apl036/afilias
%dir %{fe2basedir}/config/job/apl036/ari
%dir %{fe2basedir}/config/job/apl036/gmo
%dir %{fe2basedir}/config/job/apl036/neustar
%dir %{fe2basedir}/config/job/apl036/verisign
%dir %{fe2basedir}/config/job/apl066
%dir %{fe2basedir}/config/job/apl066/afilias
%dir %{fe2basedir}/config/job/apl066/ari
%dir %{fe2basedir}/config/job/apl066/gmo
%dir %{fe2basedir}/config/job/apl066/neustar
%dir %{fe2basedir}/config/job/apl066/verisign
%dir %{fe2basedir}/config/job/apl083
%dir %{fe2basedir}/config/job/apl083/afilias
%dir %{fe2basedir}/config/job/apl083/ari
%dir %{fe2basedir}/config/job/apl083/gmo
%dir %{fe2basedir}/config/job/apl083/neustar
%dir %{fe2basedir}/config/job/apl083/verisign
%dir %{fe2basedir}/config/job/apl087
%dir %{fe2basedir}/config/job/apl087/afilias
%dir %{fe2basedir}/config/job/apl087/ari
%dir %{fe2basedir}/config/job/apl087/gmo
%dir %{fe2basedir}/config/job/apl087/neustar
%dir %{fe2basedir}/config/job/apl087/verisign
%dir %{fe2basedir}/config/job/mon001
%dir %{fe2basedir}/config/job/mon001/afilias
%dir %{fe2basedir}/config/job/mon001/ari
%dir %{fe2basedir}/config/job/mon001/gmo
%dir %{fe2basedir}/config/job/mon001/neustar
%dir %{fe2basedir}/config/job/mon001/verisign
%{fe2basedir}/scenario.zip
%{fe2basedir}/config/job/apl002/afilias/rtk.properties
%{fe2basedir}/config/job/apl002/ari/logconfig.xml
%{fe2basedir}/config/job/apl002/gmo/rtk.properties
%{fe2basedir}/config/job/apl002/neustar/logconfig.xml
%{fe2basedir}/config/job/apl002/verisign/logconfig.xml
%{fe2basedir}/config/job/apl009/afilias/rtk.properties
%{fe2basedir}/config/job/apl009/ari/logconfig.xml
%{fe2basedir}/config/job/apl009/gmo/rtk.properties
%{fe2basedir}/config/job/apl009/neustar/logconfig.xml
%{fe2basedir}/config/job/apl009/verisign/logconfig.xml
%{fe2basedir}/config/job/apl010/afilias/rtk.properties
%{fe2basedir}/config/job/apl010/ari/logconfig.xml
%{fe2basedir}/config/job/apl010/gmo/rtk.properties
%{fe2basedir}/config/job/apl010/neustar/logconfig.xml
%{fe2basedir}/config/job/apl010/verisign/logconfig.xml
%{fe2basedir}/config/job/apl036/afilias/rtk.properties
%{fe2basedir}/config/job/apl036/ari/logconfig.xml
%{fe2basedir}/config/job/apl036/gmo/rtk.properties
%{fe2basedir}/config/job/apl036/neustar/logconfig.xml
%{fe2basedir}/config/job/apl036/verisign/logconfig.xml
%{fe2basedir}/config/job/apl066/afilias/rtk.properties
%{fe2basedir}/config/job/apl066/ari/logconfig.xml
%{fe2basedir}/config/job/apl066/gmo/rtk.properties
%{fe2basedir}/config/job/apl066/neustar/logconfig.xml
%{fe2basedir}/config/job/apl066/verisign/logconfig.xml
%{fe2basedir}/config/job/apl083/afilias/rtk.properties
%{fe2basedir}/config/job/apl083/ari/logconfig.xml
%{fe2basedir}/config/job/apl083/gmo/rtk.properties
%{fe2basedir}/config/job/apl083/neustar/logconfig.xml
%{fe2basedir}/config/job/apl083/verisign/logconfig.xml
%{fe2basedir}/config/job/apl087/afilias/rtk.properties
%{fe2basedir}/config/job/apl087/ari/logconfig.xml
%{fe2basedir}/config/job/apl087/gmo/rtk.properties
%{fe2basedir}/config/job/apl087/neustar/logconfig.xml
%{fe2basedir}/config/job/apl087/verisign/logconfig.xml
%{fe2basedir}/config/job/mon001/afilias/rtk.properties
%{fe2basedir}/config/job/mon001/ari/logconfig.xml
%{fe2basedir}/config/job/mon001/gmo/rtk.properties
%{fe2basedir}/config/job/mon001/neustar/logconfig.xml
%{fe2basedir}/config/job/mon001/verisign/logconfig.xml
%{fe2basedir}/config/job/gjp_transaction.xml
%{fe2basedir}/config/job/job_*_log4j.xml

%files -n %{name}-%{agency_package}-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/%{agency_world}
%{fe1appsdir}/%{agency_world}.war

%files -n %{name}-%{agency_package}-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/%{agency_world}
%{fe2appsdir}/%{agency_world}.war

%changelog

* Wed Nov 24 2021  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver       20211124144253
- update: gtld_conf_tomcat_ver    20211124144253

* Mon Aug 30 2021  Atsushi Furuta <furuta@jprs.co.jp>
- update for pasta DEMO service

* Thu Sep 27 2018  Satomi Yamashita  <s-yamashita@jprs.co.jp>
- update: install section config file

* Tue Aug 14 2018 Sumie Satou <su-sato@jprs.co.jp>
- update: /usr/local/apache-ant-1.10.1/bin/ant -> /usr/local/ant/bin/ant

* Wed Apr 4 2018 Kouji Takahashi <ko-takahashi@jprs.co.jp>
- add: ari/ config directry
- add: ari/logconfig.xml file

* Fri Mar 23 2018 Kouji Takahashi <ko-takahashi@jprs.co.jp>
- update: gtld_conf_app_ver     20180323160709

* Tue Mar 20 2018 Kouji Takahashi <ko-takahashi@jprs.co.jp>
- delete: gtld-app-whois2016-cmd packages
- delete: gtld-app-whois2016-web packages
- delete: gtld-app-gtld-whois2016-cmd packages
- add: debug_package
- add: __jar_repack
- delete: BuildRoot

* Wed Nov  1 2017  Yoichi Komuro  <y-komuro@jprs.co.jp>
- update: gtld_conf_app_ver     20171101181223
- update: gtld_conf_tomcat_ver  20171101181223

* Tue Oct 11 2016 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver            20161011112035

* Wed Jul 27 2016 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- add: whois2016-cmd packages
- add: whois2016-web packages
- add: gtld-whois2016-cmd packages

* Thu Nov 26 2015  Shingo Mizoi  <s-mizoi@jprs.co.jp>
- update: JAVA_HOME /usr/local/jdk1.8/
- update: JAR_BIN   /usr/local/jdk1.8/bin/jar

* Fri Oct  9 2015 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- remove: gtld-dispatch-whois-cmd packages
- remove: gtld-dispatch-whois-web packages

* Tue Sep 30 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- add: agent-jpp-pass packages
- add: agent-web-pass packages

* Mon Aug 11 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- add: gmo conf file

* Tue Jul 15 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- add: gtld-dispatch-whois-cmd packages
- add: gtld-dispatch-whois-web packages
- add: gtld-whois-cmd packages

* Thu Mar 13 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: chmod 0755 ./scenario/job/dr/bin/*.sh

* Fri Mar 7 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update  gtld_conf_app_ver       20140306215800

* Mon Jan 28 2013  Atsushi Furuta  <furuta@jprs.co.jp>
- add chmod 0755 ./scenario/job/sbin/*

* Fri Nov 9 2012  Atsushi Furuta  <furuta@jprs.co.jp>
- revert  gtld_conf_app_ver       20120411154945

* Fri Nov 9 2012  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver     20121109130634
- update: JAVA_HOME /usr/local/jdk1.6.0_37/
- update: JAR_BIN   /usr/local/jdk1.6.0_37/bin/jar

* Wed Apr 11 2012 Atsushi Furuta <furuta@jprs.co.jp>
- update  gtld_conf_app_ver       20120411154945

* Wed Apr 11 2012 Atsushi Furuta <furuta@jprs.co.jp>
- update config tag

* Fri Mar 16 2012 k-kosuga <k-kosuga@jprs.co.jp>
- first release

