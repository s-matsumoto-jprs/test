# Conditional build
#

#
# rpmbuild -ba ~/rpm/SPECS/gtld-app.spec \
#              --define='version 20110804200913' \
#              --define='release PIW.019.REAL.REL'
#
%define world           real
%define fe1		f1
%define fe1basedir	/nfs/gtd/data/%{fe1}/pasta0/
%define fe1appsdir	%{fe1basedir}/servlet/tomcat/webapps/

%define fe2		f2
%define fe2basedir	/nfs/gtd/data/%{fe2}/pasta0/
%define fe2appsdir	%{fe2basedir}/servlet/tomcat/webapps/

%define privatedir	/nfs/gtd/share/private/system/pasta0/
%define publicdir	/nfs/gtd/share/public/system/pasta0/

%define agency_package     agency
%define agency_world       gtd-%{agency_package}

%define gtld_conf_app_ver       20211124144253
%define gtld_conf_tomcat_ver    20211124144253

%define debug_package %{nil}
%define __jar_repack %{nil}

%bcond_with branch

Summary:	gTLD Registrar System
Summary(ja):	gTLD Registrar System
Name:		gtld-app
Version:	%{version}
Release:	%{release}
License:	Copyright(c) 2010-2011 JPRS
Group:		Applications/Internet/Registrar

%description
PASTA is a gTLD registrar system.

###
### gtld-app-common
###
%package -n %{name}-common
Summary:	registrar transaction system common
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app >= %{gtld_conf_app_ver}

%description -n %{name}-common
PASTA - registrar jpp system common

###
### gtld-app-agent-jpp
###
%package -n %{name}-agent-jpp-%{fe1}
Summary:	registrar transaction system for agents for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-jpp-%{fe1}
PASTA - registrar jpp system for agents for f1

%package -n %{name}-agent-jpp-%{fe2}
Summary:        registrar transaction system for agents for f2
Group:          Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-jpp-%{fe2}
PASTA - registrar jpp system for agents for f2

###
### gtld-app-agent-jpp-pass
###
%package -n %{name}-agent-jpp-pass-%{fe1}
Summary:	registrar transaction system for agents for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-jpp-pass-%{fe1}
PASTA - registrar jpp system for agents for f1

%package -n %{name}-agent-jpp-pass-%{fe2}
Summary:        registrar transaction system for agents for f2
Group:          Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-jpp-pass-%{fe2}
PASTA - registrar jpp-pass system for agents for f2

###
### gtld-app-agent-web
###
%package -n %{name}-agent-web-%{fe1}
Summary:	registrar web system for agents for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-%{fe1}
PASTA - registrar web system for agents for f1

%package -n %{name}-agent-web-%{fe2}
Summary:        registrar web system for agents for f2
Group:          Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-%{fe2}
PASTA - registrar web system for agents for f2

###
### gtld-app-agent-web-pass
###
%package -n %{name}-agent-web-pass-%{fe1}
Summary:	registrar web system for agents for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-pass-%{fe1}
PASTA - registrar web system for agents for f1

%package -n %{name}-agent-web-pass-%{fe2}
Summary:        registrar web system for agents for f2
Group:          Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-pass-%{fe2}
PASTA - registrar web-pass system for agents for f2

###
### gtld-app-whois-web
###
%package -n %{name}-whois-web-%{fe1}
Summary:	registrar whois web system for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-whois-web-%{fe1}
PASTA - whois web system for f1

%package -n %{name}-whois-web-%{fe2}
Summary:        registrar whois web system for f2
Group:          Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-whois-web-%{fe2}
PASTA - whois web system for f2

###
### gtld-app-rdap
###
%package -n %{name}-rdap-%{fe1}
Summary:	registrar rdap system for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-rdap-%{fe1}
PASTA - rdap system for f1

%package -n %{name}-rdap-%{fe2}
Summary:	registrar rdap system for f2
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-rdap-%{fe2}
PASTA - rdap system for f2

###
### gtld-app-registrant-web
###
%package -n %{name}-registrant-web-%{fe1}
Summary:	registrar web system for registrants for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-registrant-web-%{fe1}
PASTA - registrar web system for registrants for f1

%package -n %{name}-registrant-web-%{fe2}
Summary:        registrar web system for registrants for f2
Group:          Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-registrant-web-%{fe2}
PASTA - registrar web system for registrants for f2

###
### gtld-app-internal-web
###
%package -n %{name}-internal-web-%{fe1}
Summary:	registrar web system for employees for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-internal-web-%{fe1}
PASTA - registrar web system for employees for f1

%package -n %{name}-internal-web-%{fe2}
Summary:        registrar web system for employees for f2
Group:          Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-internal-web-%{fe2}
PASTA - registrar web system for employees for f2

###
### gtld-app-resident
###
%package -n %{name}-resident-%{fe1}
Summary:	registrar resident system for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-resident-%{fe1}
PASTA - registrar resident system for f1

%package -n %{name}-resident-%{fe2}
Summary:        registrar resident system for f2
Group:          Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-resident-%{fe2}
PASTA - registrar resident system for f2

###
### gtld-app-noresident
###
%package -n %{name}-noresident-%{fe1}
Summary:	registrar noresident system for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-noresident-%{fe1}
PASTA - registrar noresident system for f1

%package -n %{name}-noresident-%{fe2}
Summary:	registrar noresident system for f2
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-noresident-%{fe2}
PASTA - registrar noresident system for f2

###
### gtld-app-queue
###
%package -n %{name}-queue-%{fe1}
Summary:	registrar queue system for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-queue-%{fe1}
PASTA - registrar queue system for f1

%package -n %{name}-queue-%{fe2}
Summary:	registrar queue system for f2
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-queue-%{fe2}
PASTA - registrar queue system for f2

###
### gtld-app-scenario
###
%package -n %{name}-scenario-%{fe1}
Summary:	registrar scenario for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-scenario-%{fe1}
PASTA - registrar scenario for f1

%package -n %{name}-scenario-%{fe2}
Summary:	registrar scenario for f2
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-scenario-%{fe2}
PASTA - registrar scenario for f2

###
### gtld-app-whois-cmd
###
%package -n %{name}-whois-cmd-%{fe1}
Summary:	registrar whois command system for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-whois-cmd-%{fe1}
PASTA - whois command system for f1

%package -n %{name}-whois-cmd-%{fe2}
Summary:	registrar whois command system for f2
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-whois-cmd-%{fe2}
PASTA - whois command system for f2

###
### gtld-app-agent-web-internal
###
%package -n %{name}-agent-web-internal-%{fe1}
Summary:	agent-web internal for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe1} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-internal-%{fe1}
PASTA - agent-web internal for f1

%package -n %{name}-agent-web-internal-%{fe2}
Summary:	agent-web internal for f2
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	gtld-conf-tomcat-%{fe2} >= %{gtld_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-agent-web-internal-%{fe2}
PASTA - agent-web internal for f2

###
### gtld-app-gtld-whois-cmd
###
%package -n %{name}-gtld-whois-cmd-%{fe1}
Summary:	gTLD whois command system for f1
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe1} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-gtld-whois-cmd-%{fe1}
PASTA - gTLD whois command system for f1

%package -n %{name}-gtld-whois-cmd-%{fe2}
Summary:	gTLD whois command system for f2
Group:		Applications/Internet/Registrar
Requires:	gtld-conf-app-%{fe2} >= %{gtld_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-gtld-whois-cmd-%{fe2}
PASTA - gTLD whois command system for f2

###
### gtld-app-agency
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
%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-agent-jpp
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/pasta-agent-jpp
%__install -p -m644 pasta-agent-jpp.war    ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 pasta-agent-jpp.war    ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-agent-jpp-pass
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/pasta-agent-jpp-pass
%__install -p -m644 pasta-agent-jpp-pass.war    ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 pasta-agent-jpp-pass.war    ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/gtd-agent-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/gtd-agent-web
%__install -p -m644 gtd-agent-web.war      ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 gtd-agent-web.war      ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/gtd-agent-web-pass
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/gtd-agent-web-pass
%__install -p -m644 gtd-agent-web-pass.war      ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 gtd-agent-web-pass.war      ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-internal-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/pasta-internal-web
%__install -p -m644 pasta-internal-web.war ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 pasta-internal-web.war ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/gtd-registrant-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/gtd-registrant-web
%__install -p -m644 gtd-registrant-web.war ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 gtd-registrant-web.war ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-resident-job
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/pasta-resident-job
%__install -p -m644 pasta-resident-job.war ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 pasta-resident-job.war ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-whois-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/pasta-whois-web
%__install -p -m644 pasta-whois-web.war    ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 pasta-whois-web.war    ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/pasta-rdap
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/pasta-rdap
%__install -p -m644 pasta-rdap.war    ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 pasta-rdap.war    ${RPM_BUILD_ROOT}/%{fe2appsdir}

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

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/daemon/whois
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/daemon/whois
%__install -p -m644 whoisd.zip       ${RPM_BUILD_ROOT}/%{fe1basedir}
%__install -p -m644 whoisd.zip       ${RPM_BUILD_ROOT}/%{fe2basedir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/gtd-agent-web-internal
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/gtd-agent-web-internal
%__install -p -m644 gtd-agent-web-internal.war ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 gtd-agent-web-internal.war ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/daemon/gtld-whois
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/daemon/gtld-whois
%__install -p -m644 gtld-whoisd.zip       ${RPM_BUILD_ROOT}/%{fe1basedir}
%__install -p -m644 gtld-whoisd.zip       ${RPM_BUILD_ROOT}/%{fe2basedir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/%{agency_world}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/%{agency_world}
%__install -p -m644 %{agency_world}.war      ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 %{agency_world}.war      ${RPM_BUILD_ROOT}/%{fe2appsdir}
popd

pushd ./src/domain/registrar/config/gtd-real
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/agent-jpp
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/agent-jpp-pass
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/agent-web
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/agent-web-internal
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/agent-web-pass
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/gtld-whois-cmd
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/internal-web
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/job
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/whois-cmd
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/whois-web
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/rdap
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/registrant-web
%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/config/resident-job
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/agent-jpp
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/agent-jpp-pass
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/agent-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/agent-web-internal
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/agent-web-pass
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/gtld-whois-cmd
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/internal-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/job
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/whois-cmd
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/whois-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/rdap
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/registrant-web
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/config/resident-job
%__cp -pr agent-jpp ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr agent-jpp-pass ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr agent-web ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr agent-web-internal ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr agent-web-pass ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr gtld-whois-cmd ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr internal-web ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr job ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr whois-cmd ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr whois-web ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr rdap ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr registrant-web ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr resident-job ${RPM_BUILD_ROOT}/%{fe1basedir}/config
%__cp -pr agent-jpp ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr agent-jpp-pass ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr agent-web ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr agent-web-internal ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr agent-web-pass ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr gtld-whois-cmd ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr internal-web ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr job ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr whois-cmd ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr whois-web ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr rdap ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr registrant-web ${RPM_BUILD_ROOT}/%{fe2basedir}/config
%__cp -pr resident-job ${RPM_BUILD_ROOT}/%{fe2basedir}/config
popd

pushd ./src/domain/registrar/htdocs
%__cp -pr real ${RPM_BUILD_ROOT}/%{fe1basedir}/htdocs
%__cp -pr real ${RPM_BUILD_ROOT}/%{fe2basedir}/htdocs
popd

%__install -d ${RPM_BUILD_ROOT}%{privatedir}/acc
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/acc/forms
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/acc/forms/balance
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/acc/forms/daily
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/acc/forms/monthly
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/acc/forms/quarter
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/epp
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/epp/keystore
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/escrow
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/escrow/archive
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/escrow/work
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/fb/to-bank
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/fb/work
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/fb/to-gjp
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/gnupg
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/jp1
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/jp1/work
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/agent
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/bill
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/dns-err-del
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/dnsqc
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/dom-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/dom-trans
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/dom
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/expire
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/host
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/ns-set
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/ns
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/pub
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/recover-daily
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/recover-monthly
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/redirect
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/reg-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/reg-trans
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/reg
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/registrar-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/signingkey
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/pref-spool-apply
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/lists/pref-spool-apply/tmp
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/redirect/outgoing
%__install -p m700 -d ${RPM_BUILD_ROOT}%{privatedir}/ssh
%__install -d ${RPM_BUILD_ROOT}%{privatedir}/jp1ajs/dependency
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/agent
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/bill
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/dns-err-del
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/dnsqc
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/dom-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/dom-trans
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/dom
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/expire
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/host
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/ns-set
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/ns
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/pub
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/recover-daily
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/recover-monthly
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/redirect
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/reg-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/reg-trans
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/reg
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/registrar-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{publicdir}/lists/signingkey

%pre -n %{name}-agent-jpp-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-agent-jpp/*

%pre -n %{name}-agent-jpp-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-agent-jpp/*

%pre -n %{name}-agent-jpp-pass-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-agent-jpp-pass/*

%pre -n %{name}-agent-jpp-pass-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-agent-jpp-pass/*

%pre -n %{name}-agent-web-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-agent-web/*

%pre -n %{name}-agent-web-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-agent-web/*

%pre -n %{name}-agent-web-pass-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-agent-web-pass/*

%pre -n %{name}-agent-web-pass-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-agent-web-pass/*

%pre -n %{name}-internal-web-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-internal-web/*

%pre -n %{name}-internal-web-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-internal-web/*

%pre -n %{name}-registrant-web-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-registrant-web/*

%pre -n %{name}-registrant-web-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-registrant-web/*

%pre -n %{name}-resident-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-resident-job/*

%pre -n %{name}-resident-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-resident-job/*

%pre -n %{name}-whois-web-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-whois-web/*

%pre -n %{name}-whois-web-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-whois-web/*

%pre -n %{name}-rdap-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-rdap/*

%pre -n %{name}-rdap-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-rdap/*

%pre -n %{name}-agent-web-internal-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-agent-web-internal/*

%pre -n %{name}-agent-web-internal-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-agent-web-internal/*

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

%pre -n %{name}-whois-cmd-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/whois/*

%pre -n %{name}-whois-cmd-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/daemon/whois/*

%pre -n %{name}-gtld-whois-cmd-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/gtld-whois/*

%pre -n %{name}-gtld-whois-cmd-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/daemon/gtld-whois/*

%pre -n %{name}-%{agency_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{agency_world}/*

%pre -n %{name}-%{agency_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{agency_world}/*

%preun -n %{name}-agent-jpp-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-agent-jpp/*
fi

%preun -n %{name}-agent-jpp-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-agent-jpp/*
fi

%preun -n %{name}-agent-jpp-pass-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-agent-jpp-pass/*
fi

%preun -n %{name}-agent-jpp-pass-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-agent-jpp-pass/*
fi

%preun -n %{name}-agent-web-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-agent-web/*
fi

%preun -n %{name}-agent-web-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-agent-web/*
fi

%preun -n %{name}-agent-web-pass-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-agent-web-pass/*
fi

%preun -n %{name}-agent-web-pass-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-agent-web-pass/*
fi

%preun -n %{name}-internal-web-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-internal-web/*
fi

%preun -n %{name}-internal-web-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-internal-web/*
fi

%preun -n %{name}-registrant-web-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-registrant-web/*
fi

%preun -n %{name}-registrant-web-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-registrant-web/*
fi

%preun -n %{name}-resident-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-resident-job/*
fi

%preun -n %{name}-resident-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-resident-job/*
fi

%preun -n %{name}-whois-web-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-whois-web/*
fi

%preun -n %{name}-whois-web-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-whois-web/*
fi

%preun -n %{name}-rdap-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/pasta-rdap/*
fi

%preun -n %{name}-rdap-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/pasta-rdap/*
fi

%preun -n %{name}-agent-web-internal-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/gtd-agent-web-internal/*
fi

%preun -n %{name}-agent-web-internal-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/gtd-agent-web-internal/*
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

%preun -n %{name}-whois-cmd-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/whois/*
fi

%preun -n %{name}-whois-cmd-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/daemon/whois/*
fi

%preun -n %{name}-gtld-whois-cmd-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/daemon/gtld-whois/*
fi

%preun -n %{name}-gtld-whois-cmd-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/daemon/gtld-whois/*
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
%__unzip ./pasta-agent-jpp.war -d ./pasta-agent-jpp
%__chown -Rhf pasta0:pasta0 ./pasta-agent-jpp
popd

%post -n %{name}-agent-jpp-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./pasta-agent-jpp.war -d ./pasta-agent-jpp
%__chown -Rhf pasta0:pasta0 ./pasta-agent-jpp
popd

%post -n %{name}-agent-jpp-pass-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-agent-jpp-pass.war -d ./pasta-agent-jpp-pass
%__chown -Rhf pasta0:pasta0 ./pasta-agent-jpp-pass
popd

%post -n %{name}-agent-jpp-pass-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./pasta-agent-jpp-pass.war -d ./pasta-agent-jpp-pass
%__chown -Rhf pasta0:pasta0 ./pasta-agent-jpp-pass
popd

%post -n %{name}-agent-web-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./gtd-agent-web.war -d ./gtd-agent-web
%__chown -Rhf pasta0:pasta0 ./gtd-agent-web
popd

%post -n %{name}-agent-web-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./gtd-agent-web.war -d ./gtd-agent-web
%__chown -Rhf pasta0:pasta0 ./gtd-agent-web
popd

%post -n %{name}-agent-web-pass-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./gtd-agent-web-pass.war -d ./gtd-agent-web-pass
%__chown -Rhf pasta0:pasta0 ./gtd-agent-web-pass
popd

%post -n %{name}-agent-web-pass-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./gtd-agent-web-pass.war -d ./gtd-agent-web-pass
%__chown -Rhf pasta0:pasta0 ./gtd-agent-web-pass
popd

%post -n %{name}-internal-web-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-internal-web.war -d ./pasta-internal-web
%__chown -Rhf pasta0:pasta0 ./pasta-internal-web
popd

%post -n %{name}-internal-web-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./pasta-internal-web.war -d ./pasta-internal-web
%__chown -Rhf pasta0:pasta0 ./pasta-internal-web
popd

%post -n %{name}-registrant-web-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./gtd-registrant-web.war -d ./gtd-registrant-web
%__chown -Rhf pasta0:pasta0 ./gtd-registrant-web
popd

%post -n %{name}-registrant-web-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./gtd-registrant-web.war -d ./gtd-registrant-web
%__chown -Rhf pasta0:pasta0 ./gtd-registrant-web
popd

%post -n %{name}-resident-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-resident-job.war -d ./pasta-resident-job
%__chown -Rhf pasta0:pasta0 ./pasta-resident-job
popd

%post -n %{name}-resident-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./pasta-resident-job.war -d ./pasta-resident-job
%__chown -Rhf pasta0:pasta0 ./pasta-resident-job
popd

%post -n %{name}-whois-web-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-whois-web.war -d ./pasta-whois-web
%__chown -Rhf pasta0:pasta0 ./pasta-whois-web
popd

%post -n %{name}-whois-web-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./pasta-whois-web.war -d ./pasta-whois-web
%__chown -Rhf pasta0:pasta0 ./pasta-whois-web
popd

%post -n %{name}-rdap-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./pasta-rdap.war -d ./pasta-rdap
%__chown -Rhf pasta0:pasta0 ./pasta-rdap
popd

%post -n %{name}-rdap-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./pasta-rdap.war -d ./pasta-rdap
%__chown -Rhf pasta0:pasta0 ./pasta-rdap
popd

%post -n %{name}-noresident-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}
%__unzip ./pasta-noresident.zip -d ./standalone/job
%__chown -Rhf pasta0:pasta0 ./standalone/job
popd

%post -n %{name}-agent-web-internal-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./gtd-agent-web-internal.war -d ./gtd-agent-web-internal
%__chown -Rhf pasta0:pasta0 ./gtd-agent-web-internal
popd

%post -n %{name}-agent-web-internal-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./gtd-agent-web-internal.war -d ./gtd-agent-web-internal
%__chown -Rhf pasta0:pasta0 ./gtd-agent-web-internal
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

%post -n %{name}-whois-cmd-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}
%__unzip ./whoisd.zip -d ./daemon/whois
%__chmod 0755 ./daemon/whois/bin/*.sh
%__chown -Rhf pasta0:pasta0 ./daemon/whois
popd

%post -n %{name}-whois-cmd-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}
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

%post -n %{name}-gtld-whois-cmd-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}
%__unzip ./gtld-whoisd.zip -d ./daemon/gtld-whois
%__chmod 0755 ./daemon/gtld-whois/bin/*.sh
%__chown -Rhf pasta0:pasta0 ./daemon/gtld-whois
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
%defattr(-,pasta0,pasta0,775)
%dir %{privatedir}/jp1
%defattr(-,pasta0,pasta0)
%dir %{privatedir}/acc
%dir %{privatedir}/acc/forms
%dir %{privatedir}/acc/forms/balance
%dir %{privatedir}/acc/forms/daily
%dir %{privatedir}/acc/forms/monthly
%dir %{privatedir}/acc/forms/quarter
%dir %{privatedir}/epp
%dir %{privatedir}/epp/keystore
%dir %{privatedir}/escrow
%dir %{privatedir}/escrow/archive
%dir %{privatedir}/escrow/work
%dir %{privatedir}/fb/to-bank
%dir %{privatedir}/fb/work
%dir %{privatedir}/fb/to-gjp
%dir %{privatedir}/gnupg
%dir %{privatedir}/jp1/work
%dir %{privatedir}/lists/agent
%dir %{privatedir}/lists/bill
%dir %{privatedir}/lists/dns-err-del
%dir %{privatedir}/lists/dnsqc
%dir %{privatedir}/lists/dom-trans-apply
%dir %{privatedir}/lists/dom-trans
%dir %{privatedir}/lists/dom
%dir %{privatedir}/lists/expire
%dir %{privatedir}/lists/host
%dir %{privatedir}/lists/ns-set
%dir %{privatedir}/lists/ns
%dir %{privatedir}/lists/pub
%dir %{privatedir}/lists/recover-daily
%dir %{privatedir}/lists/recover-monthly
%dir %{privatedir}/lists/redirect
%dir %{privatedir}/lists/reg-trans-apply
%dir %{privatedir}/lists/reg-trans
%dir %{privatedir}/lists/reg
%dir %{privatedir}/lists/registrar-trans-apply
%dir %{privatedir}/lists/signingkey
%dir %{privatedir}/lists/pref-spool-apply
%dir %{privatedir}/lists/pref-spool-apply/tmp
%dir %{privatedir}/redirect/outgoing
%dir %{privatedir}/jp1ajs/dependency
%dir %{publicdir}/lists
%dir %{publicdir}/lists/agent
%dir %{publicdir}/lists/bill
%dir %{publicdir}/lists/dns-err-del
%dir %{publicdir}/lists/dnsqc
%dir %{publicdir}/lists/dom-trans-apply
%dir %{publicdir}/lists/dom-trans
%dir %{publicdir}/lists/dom
%dir %{publicdir}/lists/expire
%dir %{publicdir}/lists/host
%dir %{publicdir}/lists/ns-set
%dir %{publicdir}/lists/ns
%dir %{publicdir}/lists/pub
%dir %{publicdir}/lists/recover-daily
%dir %{publicdir}/lists/recover-monthly
%dir %{publicdir}/lists/redirect
%dir %{publicdir}/lists/reg-trans-apply
%dir %{publicdir}/lists/reg-trans
%dir %{publicdir}/lists/reg
%dir %{publicdir}/lists/registrar-trans-apply
%dir %{publicdir}/lists/signingkey
%defattr(-,pasta0,pasta0,700)
%dir %{privatedir}/ssh


%files -n %{name}-agent-jpp-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/pasta-agent-jpp
%dir %{fe1basedir}/config/agent-jpp
%dir %{fe1basedir}/config/agent-jpp/afilias
%dir %{fe1basedir}/config/agent-jpp/ari
%dir %{fe1basedir}/config/agent-jpp/gmo
%dir %{fe1basedir}/config/agent-jpp/neustar
%dir %{fe1basedir}/config/agent-jpp/verisign
%{fe1appsdir}/pasta-agent-jpp.war
%{fe1basedir}/config/agent-jpp/afilias/rtk.properties
%{fe1basedir}/config/agent-jpp/ari/logconfig.xml
%{fe1basedir}/config/agent-jpp/gmo/rtk.properties
%{fe1basedir}/config/agent-jpp/neustar/logconfig.xml
%{fe1basedir}/config/agent-jpp/verisign/logconfig.xml
%{fe1basedir}/config/agent-jpp/gjp_transaction.xml
%{fe1basedir}/config/agent-jpp/log4j.xml

%files -n %{name}-agent-jpp-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/pasta-agent-jpp
%dir %{fe2basedir}/config/agent-jpp
%dir %{fe2basedir}/config/agent-jpp/afilias
%dir %{fe2basedir}/config/agent-jpp/ari
%dir %{fe2basedir}/config/agent-jpp/gmo
%dir %{fe2basedir}/config/agent-jpp/neustar
%dir %{fe2basedir}/config/agent-jpp/verisign
%{fe2appsdir}/pasta-agent-jpp.war
%{fe2basedir}/config/agent-jpp/afilias/rtk.properties
%{fe2basedir}/config/agent-jpp/ari/logconfig.xml
%{fe2basedir}/config/agent-jpp/gmo/rtk.properties
%{fe2basedir}/config/agent-jpp/neustar/logconfig.xml
%{fe2basedir}/config/agent-jpp/verisign/logconfig.xml
%{fe2basedir}/config/agent-jpp/gjp_transaction.xml
%{fe2basedir}/config/agent-jpp/log4j.xml

%files -n %{name}-agent-jpp-pass-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/pasta-agent-jpp-pass
%dir %{fe1basedir}/config/agent-jpp-pass
%dir %{fe1basedir}/config/agent-jpp-pass/afilias
%dir %{fe1basedir}/config/agent-jpp-pass/ari
%dir %{fe1basedir}/config/agent-jpp-pass/gmo
%dir %{fe1basedir}/config/agent-jpp-pass/neustar
%dir %{fe1basedir}/config/agent-jpp-pass/verisign
%{fe1appsdir}/pasta-agent-jpp-pass.war
%{fe1basedir}/config/agent-jpp-pass/afilias/rtk.properties
%{fe1basedir}/config/agent-jpp-pass/ari/logconfig.xml
%{fe1basedir}/config/agent-jpp-pass/gmo/rtk.properties
%{fe1basedir}/config/agent-jpp-pass/neustar/logconfig.xml
%{fe1basedir}/config/agent-jpp-pass/verisign/logconfig.xml
%{fe1basedir}/config/agent-jpp-pass/gjp_transaction.xml
%{fe1basedir}/config/agent-jpp-pass/log4j.xml

%files -n %{name}-agent-jpp-pass-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/pasta-agent-jpp-pass
%dir %{fe2basedir}/config/agent-jpp-pass
%dir %{fe2basedir}/config/agent-jpp-pass/afilias
%dir %{fe2basedir}/config/agent-jpp-pass/ari
%dir %{fe2basedir}/config/agent-jpp-pass/gmo
%dir %{fe2basedir}/config/agent-jpp-pass/neustar
%dir %{fe2basedir}/config/agent-jpp-pass/verisign
%{fe2appsdir}/pasta-agent-jpp-pass.war
%{fe2basedir}/config/agent-jpp-pass/afilias/rtk.properties
%{fe2basedir}/config/agent-jpp-pass/ari/logconfig.xml
%{fe2basedir}/config/agent-jpp-pass/gmo/rtk.properties
%{fe2basedir}/config/agent-jpp-pass/neustar/logconfig.xml
%{fe2basedir}/config/agent-jpp-pass/verisign/logconfig.xml
%{fe2basedir}/config/agent-jpp-pass/gjp_transaction.xml
%{fe2basedir}/config/agent-jpp-pass/log4j.xml

%files -n %{name}-agent-web-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/gtd-agent-web
%dir %{fe1basedir}/config/agent-web
%dir %{fe1basedir}/config/agent-web/afilias
%dir %{fe1basedir}/config/agent-web/ari
%dir %{fe1basedir}/config/agent-web/gmo
%dir %{fe1basedir}/config/agent-web/neustar
%dir %{fe1basedir}/config/agent-web/verisign
%dir %{fe1basedir}/htdocs/gtd-agent-web
%dir %{fe1basedir}/htdocs/gtd-agent-web/gtd-agent-web
%{fe1appsdir}/gtd-agent-web.war
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
%dir %{fe2appsdir}/gtd-agent-web
%dir %{fe2basedir}/config/agent-web
%dir %{fe2basedir}/config/agent-web/afilias
%dir %{fe2basedir}/config/agent-web/ari
%dir %{fe2basedir}/config/agent-web/gmo
%dir %{fe2basedir}/config/agent-web/neustar
%dir %{fe2basedir}/config/agent-web/verisign
%dir %{fe2basedir}/htdocs/gtd-agent-web
%dir %{fe2basedir}/htdocs/gtd-agent-web/gtd-agent-web
%{fe2appsdir}/gtd-agent-web.war
%{fe2basedir}/config/agent-web/afilias/rtk.properties
%{fe2basedir}/config/agent-web/ari/logconfig.xml
%{fe2basedir}/config/agent-web/gmo/rtk.properties
%{fe2basedir}/config/agent-web/neustar/logconfig.xml
%{fe2basedir}/config/agent-web/verisign/logconfig.xml
%{fe2basedir}/config/agent-web/gjp_transaction.xml
%{fe2basedir}/config/agent-web/log4j.xml
%{fe2basedir}/htdocs/gtd-agent-web/img
%{fe2basedir}/htdocs/gtd-agent-web/gtd-agent-web/img

%files -n %{name}-agent-web-pass-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/gtd-agent-web-pass
%dir %{fe1basedir}/config/agent-web-pass
%dir %{fe1basedir}/config/agent-web-pass/afilias
%dir %{fe1basedir}/config/agent-web-pass/ari
%dir %{fe1basedir}/config/agent-web-pass/gmo
%dir %{fe1basedir}/config/agent-web-pass/neustar
%dir %{fe1basedir}/config/agent-web-pass/verisign
%dir %{fe1basedir}/htdocs/gtd-agent-web-pass
%dir %{fe1basedir}/htdocs/gtd-agent-web-pass/gtd-agent-web-pass
%{fe1appsdir}/gtd-agent-web-pass.war
%{fe1basedir}/config/agent-web-pass/afilias/rtk.properties
%{fe1basedir}/config/agent-web-pass/ari/logconfig.xml
%{fe1basedir}/config/agent-web-pass/gmo/rtk.properties
%{fe1basedir}/config/agent-web-pass/neustar/logconfig.xml
%{fe1basedir}/config/agent-web-pass/verisign/logconfig.xml
%{fe1basedir}/config/agent-web-pass/gjp_transaction.xml
%{fe1basedir}/config/agent-web-pass/log4j.xml
%{fe1basedir}/htdocs/gtd-agent-web-pass/img
%{fe1basedir}/htdocs/gtd-agent-web-pass/gtd-agent-web-pass/img

%files -n %{name}-agent-web-pass-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/gtd-agent-web-pass
%dir %{fe2basedir}/config/agent-web-pass
%dir %{fe2basedir}/config/agent-web-pass/afilias
%dir %{fe2basedir}/config/agent-web-pass/ari
%dir %{fe2basedir}/config/agent-web-pass/gmo
%dir %{fe2basedir}/config/agent-web-pass/neustar
%dir %{fe2basedir}/config/agent-web-pass/verisign
%dir %{fe2basedir}/htdocs/gtd-agent-web-pass
%dir %{fe2basedir}/htdocs/gtd-agent-web-pass/gtd-agent-web-pass
%{fe2appsdir}/gtd-agent-web-pass.war
%{fe2basedir}/config/agent-web-pass/afilias/rtk.properties
%{fe2basedir}/config/agent-web-pass/ari/logconfig.xml
%{fe2basedir}/config/agent-web-pass/gmo/rtk.properties
%{fe2basedir}/config/agent-web-pass/neustar/logconfig.xml
%{fe2basedir}/config/agent-web-pass/verisign/logconfig.xml
%{fe2basedir}/config/agent-web-pass/gjp_transaction.xml
%{fe2basedir}/config/agent-web-pass/log4j.xml
%{fe2basedir}/htdocs/gtd-agent-web-pass/img
%{fe2basedir}/htdocs/gtd-agent-web-pass/gtd-agent-web-pass/img

%files -n %{name}-internal-web-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/pasta-internal-web
%dir %{fe1basedir}/config/internal-web
%dir %{fe1basedir}/htdocs/pasta-internal-web
%dir %{fe1basedir}/htdocs/pasta-internal-web/pasta-internal-web
%{fe1appsdir}/pasta-internal-web.war
%{fe1basedir}/config/internal-web/gjp_transaction.xml
%{fe1basedir}/config/internal-web/log4j.xml
%{fe1basedir}/htdocs/pasta-internal-web/img
%{fe1basedir}/htdocs/pasta-internal-web/pasta-internal-web/img

%files -n %{name}-internal-web-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/pasta-internal-web
%dir %{fe2basedir}/config/internal-web
%dir %{fe2basedir}/htdocs/pasta-internal-web
%dir %{fe2basedir}/htdocs/pasta-internal-web/pasta-internal-web
%{fe2appsdir}/pasta-internal-web.war
%{fe2basedir}/config/internal-web/gjp_transaction.xml
%{fe2basedir}/config/internal-web/log4j.xml
%{fe2basedir}/htdocs/pasta-internal-web/img
%{fe2basedir}/htdocs/pasta-internal-web/pasta-internal-web/img


%files -n %{name}-registrant-web-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/gtd-registrant-web
%dir %{fe1basedir}/config/registrant-web
%dir %{fe1basedir}/config/registrant-web/afilias
%dir %{fe1basedir}/config/registrant-web/ari
%dir %{fe1basedir}/config/registrant-web/gmo
%dir %{fe1basedir}/config/registrant-web/neustar
%dir %{fe1basedir}/config/registrant-web/verisign
%dir %{fe1basedir}/htdocs/gtd-registrant-web
%dir %{fe1basedir}/htdocs/gtd-registrant-web/gtd-registrant-web
%dir %{fe1basedir}/htdocs/gtd-agent-web/gtd-registrant-web
%{fe1appsdir}/gtd-registrant-web.war
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
%dir %{fe2appsdir}/gtd-registrant-web
%dir %{fe2basedir}/config/registrant-web
%dir %{fe2basedir}/config/registrant-web/afilias
%dir %{fe2basedir}/config/registrant-web/ari
%dir %{fe2basedir}/config/registrant-web/gmo
%dir %{fe2basedir}/config/registrant-web/neustar
%dir %{fe2basedir}/config/registrant-web/verisign
%dir %{fe2basedir}/htdocs/gtd-registrant-web
%dir %{fe2basedir}/htdocs/gtd-registrant-web/gtd-registrant-web
%dir %{fe2basedir}/htdocs/gtd-agent-web/gtd-registrant-web
%{fe2appsdir}/gtd-registrant-web.war
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
%dir %{fe1appsdir}/pasta-resident-job
%dir %{fe1basedir}/config/resident-job
%dir %{fe1basedir}/config/resident-job/afilias
%dir %{fe1basedir}/config/resident-job/ari
%dir %{fe1basedir}/config/resident-job/gmo
%dir %{fe1basedir}/config/resident-job/neustar
%dir %{fe1basedir}/config/resident-job/verisign
%{fe1appsdir}/pasta-resident-job.war
%{fe1basedir}/config/resident-job/afilias/rtk.properties
%{fe1basedir}/config/resident-job/ari/logconfig.xml
%{fe1basedir}/config/resident-job/gmo/rtk.properties
%{fe1basedir}/config/resident-job/neustar/logconfig.xml
%{fe1basedir}/config/resident-job/verisign/logconfig.xml
%{fe1basedir}/config/resident-job/log4j.xml

%files -n %{name}-resident-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/pasta-resident-job
%dir %{fe2basedir}/config/resident-job
%dir %{fe2basedir}/config/resident-job/afilias
%dir %{fe2basedir}/config/resident-job/ari
%dir %{fe2basedir}/config/resident-job/gmo
%dir %{fe2basedir}/config/resident-job/neustar
%dir %{fe2basedir}/config/resident-job/verisign
%{fe2appsdir}/pasta-resident-job.war
%{fe2basedir}/config/resident-job/afilias/rtk.properties
%{fe2basedir}/config/resident-job/ari/logconfig.xml
%{fe2basedir}/config/resident-job/gmo/rtk.properties
%{fe2basedir}/config/resident-job/neustar/logconfig.xml
%{fe2basedir}/config/resident-job/verisign/logconfig.xml
%{fe2basedir}/config/resident-job/log4j.xml


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

%files -n %{name}-whois-web-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/pasta-whois-web
%dir %{fe2basedir}/config/whois-web
%dir %{fe2basedir}/htdocs/pasta-whois-web
%{fe2appsdir}/pasta-whois-web.war
%{fe2basedir}/config/whois-web/log4j.xml
%{fe2basedir}/htdocs/pasta-whois-web/img
%{fe2basedir}/htdocs/pasta-whois-web/css
%{fe2basedir}/htdocs/pasta-whois-web/html
%{fe2basedir}/htdocs/pasta-whois-web/robots.txt


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

%files -n %{name}-rdap-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2appsdir}/pasta-rdap
%dir %{fe2basedir}/config/rdap
%dir %{fe2basedir}/htdocs/pasta-rdap
%dir %{fe2basedir}/htdocs/pasta-www-rdap
%dir %{fe2basedir}/htdocs/pasta-www-rdap/docs
%{fe2basedir}/htdocs/pasta-www-rdap/index.html
%{fe2appsdir}/pasta-rdap.war
%{fe2basedir}/config/rdap/log4j.xml


%files -n %{name}-agent-web-internal-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1appsdir}/gtd-agent-web-internal
%dir %{fe1basedir}/config/agent-web-internal
%dir %{fe1basedir}/config/agent-web-internal/afilias
%dir %{fe1basedir}/config/agent-web-internal/ari
%dir %{fe1basedir}/config/agent-web-internal/gmo
%dir %{fe1basedir}/config/agent-web-internal/neustar
%dir %{fe1basedir}/config/agent-web-internal/verisign
%dir %{fe1basedir}/htdocs/gtd-agent-web-internal
%dir %{fe1basedir}/htdocs/gtd-agent-web-internal/gtd-agent-web-internal
%{fe1appsdir}/gtd-agent-web-internal.war
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
%dir %{fe2appsdir}/gtd-agent-web-internal
%dir %{fe2basedir}/config/agent-web-internal
%dir %{fe2basedir}/config/agent-web-internal/afilias
%dir %{fe2basedir}/config/agent-web-internal/ari
%dir %{fe2basedir}/config/agent-web-internal/gmo
%dir %{fe2basedir}/config/agent-web-internal/neustar
%dir %{fe2basedir}/config/agent-web-internal/verisign
%dir %{fe2basedir}/htdocs/gtd-agent-web-internal
%dir %{fe2basedir}/htdocs/gtd-agent-web-internal/gtd-agent-web-internal
%{fe2appsdir}/gtd-agent-web-internal.war
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


%files -n %{name}-whois-cmd-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1basedir}/daemon
%dir %{fe1basedir}/daemon/whois
%dir %{fe1basedir}/config/whois-cmd
%{fe1basedir}/whoisd.zip
%{fe1basedir}/config/whois-cmd/log4j.xml

%files -n %{name}-whois-cmd-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2basedir}/daemon
%dir %{fe2basedir}/daemon/whois
%dir %{fe2basedir}/config/whois-cmd
%{fe2basedir}/whoisd.zip
%{fe2basedir}/config/whois-cmd/log4j.xml


%files -n %{name}-gtld-whois-cmd-%{fe1}
%defattr(-,pasta0,pasta0)
%dir %{fe1basedir}/daemon
%dir %{fe1basedir}/daemon/gtld-whois
%dir %{fe1basedir}/config/gtld-whois-cmd
%{fe1basedir}/gtld-whoisd.zip
%{fe1basedir}/config/gtld-whois-cmd/log4j.xml

%files -n %{name}-gtld-whois-cmd-%{fe2}
%defattr(-,pasta0,pasta0)
%dir %{fe2basedir}/daemon
%dir %{fe2basedir}/daemon/gtld-whois
%dir %{fe2basedir}/config/gtld-whois-cmd
%{fe2basedir}/gtld-whoisd.zip
%{fe2basedir}/config/gtld-whois-cmd/log4j.xml


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

* Fri Nov 12 2021 Daisuke Ito <da-ito@jprs.co.jp>
- update: gtld_conf_app_ver 20211111205145
- update: gtld_conf_tomcat_ver 20211111205145

* Mon Aug 30 2021  Atsushi Furuta <furuta@jprs.co.jp>
- update for pasta DEMO service

* Thu Apr 1 2021  Shingo Ogawa  <sh-ogawa@jprs.co.jp>
- update: gtld_conf_app_ver     20210331214032
- update: gtld_conf_tomcat_ver  20210331214032

* Wed Jul 10 2019  Tsutomu Sakuma  <t-sakuma@jprs.co.jp>
- add: htdocs/pasta-rdap directry

* Wed Oct 24 2018  Satomi Yamashita  <s-yamashita@jprs.co.jp>
- add: gtld-app-rdap packages

* Thu Sep 27 2018  Satomi Yamashita  <s-yamashita@jprs.co.jp>
- update: install section config file

* Tue Apr 24 2018  Sumie Satou  <su-sato@jprs.co.jp>
- update: gtld_conf_app_ver     20180423192957
- update: gtld_conf_tomcat_ver  20180423192957

* Fri Mar 23 2018 Kouji Takahashi <ko-takahashi@jprs.co.jp>
- update: gtld_conf_app_ver     20180323162820
- update: gtld_conf_tomcat_ver  20180323162820

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

* Fri Oct 27 2017  Yoichi Komuro  <y-komuro@jprs.co.jp>
- add: ari/ config directry
- add: ari/logconfig.xml file
- update: /usr/local/apache-ant-1.10.1/bin/ant -> /usr/local/ant/bin/ant

* Mon Sep  4 2017  Yoichi Komuro  <y-komuro@jprs.co.jp>
- add: /jp1 directry

* Thu Aug 24 2017  Yoichi Komuro  <y-komuro@jprs.co.jp>
- update: gtld_conf_app_ver     20170823161251
- update: gtld_conf_tomcat_ver  20170823161251

* Wed Aug  9 2017  Nobuyoshi Tanaka  <n-tanaka@jprs.co.jp>
- update: gtld_conf_app_ver     20170804190424
- update: gtld_conf_tomcat_ver  20170804190424

* Tue Aug  1 2017  Nobuyoshi Tanaka  <n-tanaka@jprs.co.jp>
- add: /config/job/apl087 directry

* Wed Jun 28 2017  Yoichi Komuro  <y-komuro@jprs.co.jp>
- update: gtld_conf_app_ver     20170628131250
- update: gtld_conf_tomcat_ver  20170628131250

* Fri May 12 2017  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver     20170511182814
- update: gtld_conf_tomcat_ver  20170511182814

* Wed Aug 10 2016  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver     20160809160001
- update: gtld_conf_tomcat_ver  20160809160001

* Mon May 16 2016  Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20160421174208
- update: gtld_conf_tomcat_ver  20160421174208

* Mon Jan 25 2016  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver     20160122185046
- update: gtld_conf_tomcat_ver  20160122185046

* Thu Dec 17 2015  Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20151216172505
- update: gtld_conf_tomcat_ver  20151216172505

* Mon Dec  7 2015  Atsushi Furuta  <furuta@jprs.co.jp>
- add: gtld-app-whois2016-cmd packages
- add: gtld-app-whois2016-web packages
- add: gtld-app-gtld-whois2016-cmd packages

* Thu Nov 26 2015  Shingo Mizoi  <s-mizoi@jprs.co.jp>
- update: JAVA_HOME /usr/local/jdk1.8/ 
- update: JAR_BIN   /usr/local/jdk1.8/bin/jar

* Fri Nov 20 2015 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20151120104749
- update: gtld_conf_tomcat_ver  20151120104749

* Wed Oct 28 2015 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20151027112753
- update: gtld_conf_tomcat_ver  20151027112753

* Fri Oct  2 2015  Atsushi Furuta  <furuta@jprs.co.jp>
- remove: gtld-dispatch-whois-cmd packages
- remove: gtld-dispatch-whois-web packages

* Tue Jun 30 2015 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20150630105105
- update: gtld_conf_tomcat_ver  20150630105105

* Fri May 8 2015 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20150501190247
- update: gtld_conf_tomcat_ver  20150501190247

* Thu Apr 16 2015 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20150416133341
- update: gtld_conf_tomcat_ver  20150416133341

* Tue Oct 28 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20141028113328
- update: gtld_conf_tomcat_ver  20141028113328

* Tue Sep 9 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- add: gtld-app-agent-jpp-pass packages
- add: gtld-app-agent-web-pass packages
- add: gtld-app-agency packages

* Mon Jul 14 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20140714220828
- update: gtld_conf_tomcat_ver  20140714220828

* Tue Apr 15 2014  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver       20140414133128
- update: gtld_conf_tomcat_ver    20140414133128

* Thu Mar 27 2014  Atsushi Furuta  <furuta@jprs.co.jp>
- add: gtld-dispatch-whois-cmd packages
- add: gtld-dispatch-whois-web packages
- add: gtld-whois-cmd packages

* Thu Mar 13 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20140313120739
- update: gtld_conf_tomcat_ver  20140313120739

* Fri Mar 7 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20140306215800
- update: gtld_conf_tomcat_ver  20140306215800

* Tue Feb 25 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: chmod 0755 ./scenario/job/dr/bin/*.sh

* Fri Jan 31 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20140130174631
- update: gtld_conf_tomcat_ver  20140130174631

* Tue Nov 19 2013 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20131119171716
- update: gtld_conf_tomcat_ver  20131119171716

* Thu Oct 10 2013 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gtld_conf_app_ver     20131008143506
- update: gtld_conf_tomcat_ver  20131008143506

* Mon Jan 28 2013  Atsushi Furuta  <furuta@jprs.co.jp>
- add chmod 0755 ./scenario/job/sbin/*

* Fri Jan 18 2013 Tomohiro Nakagawa <t-nakagw@jprs.co.jp>
- update: gtld_conf_app_ver     20130111171544
- update: gtld_conf_tomcat_ver  20130111171544

* Tue Nov 13 2012  Keisuke Kosuga  <k-kosuga@jprs.co.jp>
- update: gtld_conf_app_ver     20121113103613
- update: gtld_conf_tomcat_ver  20121113103613

* Fri Nov 9 2012  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver     20121109130634
- update: gtld_conf_tomcat_ver  20121109130634
- update: JAVA_HOME /usr/local/jdk1.6.0_37/ 
- update: JAR_BIN   /usr/local/jdk1.6.0_37/bin/jar

* Thu May 31 2012 Kentaro Iino <k-iino@jprs.co.jp>
- update: gtld_conf_app_ver     20120531132827
- update: gtld_conf_tomcat_ver  20120531132827

* Wed Apr 11 2012  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver	20120411154945
- update: gtld_conf_tomcat_ver	20120411154945

* Wed Apr 11 2012  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver	20120411095158
- update: gtld_conf_tomcat_ver	20120411095158

* Wed Mar 21 2012 Kentaro Iino <k-iino@jprs.co.jp>
- update: copy config directory real -> gtd-real

* Tue Mar 13 2012 Kentaro Iino <k-iino@jprs.co.jp>
- update: JAVA_HOME /usr/local/jdk1.6.0_31/ 
- update: JAR_BIN   /usr/local/jdk1.6.0_31/bin/jar

* Mon Dec 12 2011  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gtld_conf_app_ver	20111209164112
- update: gtld_conf_tomcat_ver	20111209164112
- update: svn url http://svn1.jprs.co.jp/system/

* Fri Dec 9 2011 NOGUCHI Shoji <noguchi@jprs.co.jp>
- modify: htdocs/pasta-whois-web/*

* Thu Nov 24 2011 NOGUCHI Shoji <noguchi@jprs.co.jp>
- add: htdocs/*

* Fri Nov 18 2011 NOGUCHI Shoji <noguchi@jprs.co.jp>
- update: gtld_conf_app_ver	20111118215641
- update: gtld_conf_tomcat_ver	20111118215641
- remove: registry.xml

* Fri Aug 26 2011 NOGUCHI Shoji <noguchi@jprs.co.jp>
- first release

