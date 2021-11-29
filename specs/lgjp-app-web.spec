# Conditional build
#

#
# rpmbuild -ba ~/rpm/SPECS/lgjp-app-web.spec \
#              --define='version 20170919203743' \
#              --define='release PIW.019.REAL.REL'
#
%define account              dotjp1
%define account_group        dotjp1
%define world                real
%define app_agent_web        agent-web
%define tld                  lgjp
%define servlet_agent_web    %{tld}-%{app_agent_web}
%define fe1                  f1
%define fe1basedir           /nfs/reg/data/%{fe1}/%{account}
%define fe1appsdir           %{fe1basedir}/servlet/webapps
%define fe1batchdir          %{fe1basedir}/%{tld}-%{app_agent_web}-batch
%define fe1servletbindir     %{fe1basedir}/servlet/bin
%define fe1servletconfdir    %{fe1basedir}/servlet/conf
%define fe2                  f2
%define fe2basedir           /nfs/reg/data/%{fe2}/%{account}
%define fe2appsdir           %{fe2basedir}/servlet/webapps
%define fe2batchdir          %{fe2basedir}/%{tld}-%{app_agent_web}-batch
%define fe2servletbindir     %{fe2basedir}/servlet/bin
%define fe2servletconfdir    %{fe2basedir}/servlet/conf

%define agent_web_package    agent-web
%define batch_package        batch

%bcond_with branch

Summary:     lgjp Registry System
Summary(ja): lgjp Registry System
Name:        lgjp-app-web
Version:     %{version}
Release:     %{release}
License:     Copyright(c) 2018 JPRS
Group:       Applications/Internet/Registry
BuildRoot:   %{_tmppath}/%{name}-%{version}-root

%description
lgjp Registry System

###
### lgjp-app-web-agent-web
###
%package -n %{name}-%{agent_web_package}-%{fe1}
Summary:  lgjp Registry System for f1
Group:    Applications/Internet/Registry

%description -n %{name}-%{agent_web_package}-%{fe1}
lgjp registry internal web system for f1


%package -n %{name}-%{agent_web_package}-%{fe2}
Summary:  lgjp Registry System for f2
Group:    Applications/Internet/Registry

%description -n %{name}-%{agent_web_package}-%{fe2}
lgjp registry internal web system for f2


###
### lgjp-app-web-batch
###
%package -n %{name}-%{batch_package}-%{fe1}
Summary:  lgjp Registry Batch System for f1
Group:    Applications/Internet/Registry

%description -n %{name}-%{batch_package}-%{fe1}
lgjp registry batch system for f1


%package -n %{name}-%{batch_package}-%{fe2}
Summary:  lgjp Registry Batch System for f2
Group:    Applications/Internet/Registry

%description -n %{name}-%{batch_package}-%{fe2}
lgjp registry batch system for f2


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

svn co --depth immediates http://svn1.jprs.co.jp/system/${TAG}/src/framework/jfk ./src/framework/jfk
svn co --depth immediates http://svn1.jprs.co.jp/system/${TAG}/src/domain/common ./src/domain/common
svn co --depth immediates http://svn1.jprs.co.jp/system/${TAG}/src/domain/registry-lgjp ./src/domain/registry-lgjp

svn up --set-depth infinity ./src/framework/jfk/WEB-INF
svn up --set-depth infinity ./src/framework/jfk/src
svn up --set-depth infinity ./src/domain/common/WEB-INF
svn up --set-depth infinity ./src/domain/common/src
svn up --set-depth infinity ./src/domain/registry-lgjp/lgjp
svn up --set-depth infinity ./src/domain/registry-lgjp/vendors
svn up --set-depth infinity ./src/domain/registry-lgjp/image
svn up --set-depth infinity ./src/domain/registry-lgjp/WEB-INF
svn up --set-depth infinity ./src/domain/registry-lgjp/src
svn up --set-depth infinity ./src/domain/registry-lgjp/css
svn up --set-depth infinity ./src/domain/registry-lgjp/js
svn up --set-depth infinity ./src/domain/registry-lgjp/perl5

%build
export JAVA_HOME=/usr/local/jdk1.8/
cd ./src/domain/registry-lgjp/
/usr/local/ant/bin/ant \
   -f build.domain.registry.lgjp.xml \
   -Drelease.mode=product

%install
[ "${RPM_BUILD_ROOT}" != "/" ] && %__rm -rf ${RPM_BUILD_ROOT}

export JAR_BIN=/usr/local/jdk1.8/bin/jar

### lgjp-agent-web
pushd ./src/domain/registry-lgjp/build.war/build.agent.web
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/reader
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/uploader
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/writer
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/mail
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/rrp
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/rrp/lgjp
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/generalmaster
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/prefecture
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/mail
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/xml
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/check
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/enums
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/util
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/util/batch
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/file
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/local
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/mail

#/*@@ ˆÈ‰º’Ç‰Á */
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/thread

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/config
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/data
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/lib
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/scenario
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/template
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image/lgweb
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/vendors
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/vendors/lgweb
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/css
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/css/lgweb
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/js
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/js/lgweb

%__install -p -m644 WEB-INF/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/
%__install -p -m644 WEB-INF/config/agentweb/*.dtd ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/
%__install -p -m644 WEB-INF/config/agentweb/*.properties ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/
%__install -p -m644 WEB-INF/config/agentweb/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/
%__install -p -m644 WEB-INF/data/*.txt ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/data/
%__install -p -m644 WEB-INF/lib/*.jar ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/lib/
%__install -p -m644 WEB-INF/script/*.xls ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script/
%__install -p -m644 WEB-INF/script/agentweb/*.xls ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/
%__install -p -m644 WEB-INF/script/agentweb/scenario/*.xls ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/scenario/
%__install -p -m644 WEB-INF/template/agentweb/*.html ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb/
%__install -p -m644 WEB-INF/template/agentweb/*.vm ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb/

#/*@@ ˆÈ‰º’Ç‰Á */
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/thread/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/thread/

%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/generalmaster/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/generalmaster/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/prefecture/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/prefecture/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/reader/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/reader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/uploader/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/uploader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/writer/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/writer/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/mail/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/rrp/lgjp/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/rrp/lgjp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/mail/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/xml/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/xml/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/check/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/check/*.properties ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/enums/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/enums/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/util/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/util/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/util/batch/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/util/batch/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/model/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/model/file/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/file/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/model/local/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/local/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/model/mail/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/mail/
%__install -p -m644 image/lgweb/*.gif ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image/lgweb/
%__install -p -m644 image/lgweb/*.jpg ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image/lgweb/
%__install -p -m644 css/lgweb/*.css ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/css/lgweb/
%__install -p -m644 js/lgweb/*.js ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/js/lgweb/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/reader
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/uploader
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/writer
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/mail
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/rrp
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/rrp/lgjp
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/generalmaster
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/prefecture
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/mail
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/xml
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/check
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/enums
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/util
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/util/batch
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/file
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/local
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/mail
#/*@@ ˆÈ‰º’Ç‰Á */
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/thread

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/config
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/data
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/lib
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/scenario
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/template
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image/lgweb
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/vendors
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/vendors/lgweb
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/css
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/css/lgweb
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/js
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/js/lgweb

%__install -p -m644 WEB-INF/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/
%__install -p -m644 WEB-INF/config/agentweb/*.dtd ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/
%__install -p -m644 WEB-INF/config/agentweb/*.properties ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/
%__install -p -m644 WEB-INF/config/agentweb/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/
%__install -p -m644 WEB-INF/data/*.txt ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/data/
%__install -p -m644 WEB-INF/lib/*.jar ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/lib/
%__install -p -m644 WEB-INF/script/*.xls ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script/
%__install -p -m644 WEB-INF/script/agentweb/*.xls ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/
%__install -p -m644 WEB-INF/script/agentweb/scenario/*.xls ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/scenario/
%__install -p -m644 WEB-INF/template/agentweb/*.html ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb/
%__install -p -m644 WEB-INF/template/agentweb/*.vm ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb/

#/*@@ ˆÈ‰º’Ç‰Á */
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/thread/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/agent/lgjp/web/thread/

%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/generalmaster/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/generalmaster/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/prefecture/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/constant/prefecture/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/reader/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/reader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/uploader/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/uploader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/writer/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/file/writer/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/mail/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/rrp/lgjp/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dao/rrp/lgjp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/db/regif/table/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/mail/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/xml/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/integration/dto/xml/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/check/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/check/*.properties ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/enums/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/enums/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/util/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/util/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/library/util/batch/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/library/util/batch/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/model/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/model/file/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/file/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/model/local/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/local/
%__install -p -m644 classes/jp/co/jprs/domain/registry/lgjp/common/model/mail/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/lgjp/common/model/mail/
%__install -p -m644 image/lgweb/*.gif ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image/lgweb/
%__install -p -m644 image/lgweb/*.jpg ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image/lgweb/
%__install -p -m644 css/lgweb/*.css ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/css/lgweb/
%__install -p -m644 js/lgweb/*.js ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/js/lgweb/

%__install -p -m644 dest/%{servlet_agent_web}.war ${RPM_BUILD_ROOT}%{fe1appsdir}
%__install -p -m644 dest/%{servlet_agent_web}.war ${RPM_BUILD_ROOT}%{fe2appsdir}

popd


### batch
pushd ./src/domain/registry-lgjp/build.war/build.batch
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/config
%__install -p -m644 config/*.xml ${RPM_BUILD_ROOT}%{fe1batchdir}/config/
%__install -p -m644 config/*.properties ${RPM_BUILD_ROOT}%{fe1batchdir}/config/
%__install -p -m644 config/*.dtd ${RPM_BUILD_ROOT}%{fe1batchdir}/config/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/lib
%__install -p -m644 lib/*.jar ${RPM_BUILD_ROOT}%{fe1batchdir}/lib/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/scenario/job
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/scenario/job/config
%__install -p -m755 scenario/job/*.sh ${RPM_BUILD_ROOT}%{fe1batchdir}/scenario/job/
%__install -p -m644 scenario/job/config/*.conf ${RPM_BUILD_ROOT}%{fe1batchdir}/scenario/job/config/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/template
%__install -p -m644 template/*.txt ${RPM_BUILD_ROOT}%{fe1batchdir}/template/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/bin
%__install -p -m644 perl5/bin/* ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/bin/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/etc
%__install -p -m644 perl5/etc/*.conf ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/etc/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/etc/regifrc
%__install -p -m644 perl5/etc/regifrc/* ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/etc/regifrc/
%__install -p -m644 perl5/etc/regifrc/.regifrc ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/etc/regifrc/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib
%__install -p -m644 perl5/lib/*.pm ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Jprs
%__install -p -m644 perl5/lib/Jprs/*.pm ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Jprs/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif
%__install -p -m644 perl5/lib/Regif/*.pm ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif/Column
%__install -p -m644 perl5/lib/Regif/Column/* ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif/Column/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif/Ip
%__install -p -m644 perl5/lib/Regif/Ip/* ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif/Ip/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif/Table
%__install -p -m644 perl5/lib/Regif/Table/* ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif/Table/
%__install -d ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif/Trz
%__install -p -m644 perl5/lib/Regif/Trz/* ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5/lib/Regif/Trz/

%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/config
%__install -p -m644 config/*.xml ${RPM_BUILD_ROOT}%{fe2batchdir}/config/
%__install -p -m644 config/*.properties ${RPM_BUILD_ROOT}%{fe2batchdir}/config/
%__install -p -m644 config/*.dtd ${RPM_BUILD_ROOT}%{fe2batchdir}/config/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/lib
%__install -p -m644 lib/*.jar ${RPM_BUILD_ROOT}%{fe2batchdir}/lib/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/scenario/job
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/scenario/job/config
%__install -p -m755 scenario/job/*.sh ${RPM_BUILD_ROOT}%{fe2batchdir}/scenario/job/
%__install -p -m644 scenario/job/config/*.conf ${RPM_BUILD_ROOT}%{fe2batchdir}/scenario/job/config/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/template
%__install -p -m644 template/*.txt ${RPM_BUILD_ROOT}%{fe2batchdir}/template/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/bin
%__install -p -m644 perl5/bin/* ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/bin/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/etc
%__install -p -m644 perl5/etc/*.conf ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/etc/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/etc/regifrc
%__install -p -m644 perl5/etc/regifrc/* ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/etc/regifrc/
%__install -p -m644 perl5/etc/regifrc/.regifrc ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/etc/regifrc/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib
%__install -p -m644 perl5/lib/*.pm ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Jprs
%__install -p -m644 perl5/lib/Jprs/*.pm ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Jprs/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif
%__install -p -m644 perl5/lib/Regif/*.pm ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif/Column
%__install -p -m644 perl5/lib/Regif/Column/* ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif/Column/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif/Ip
%__install -p -m644 perl5/lib/Regif/Ip/* ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif/Ip/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif/Table
%__install -p -m644 perl5/lib/Regif/Table/* ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif/Table/
%__install -d ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif/Trz
%__install -p -m644 perl5/lib/Regif/Trz/* ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5/lib/Regif/Trz/
popd

%pre -n %{name}-%{agent_web_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/*

%pre -n %{name}-%{agent_web_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/*

%pre -n %{name}-%{batch_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1batchdir}/lib
%__rm -rf ${RPM_BUILD_ROOT}%{fe1batchdir}/perl5
%__rm -rf ${RPM_BUILD_ROOT}%{fe1batchdir}/scenario
%__rm -rf ${RPM_BUILD_ROOT}%{fe1batchdir}/template

%pre -n %{name}-%{batch_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2batchdir}/lib
%__rm -rf ${RPM_BUILD_ROOT}%{fe2batchdir}/perl5
%__rm -rf ${RPM_BUILD_ROOT}%{fe2batchdir}/scenario
%__rm -rf ${RPM_BUILD_ROOT}%{fe2batchdir}/template

%clean
%__rm -rf ${RPM_BUILD_ROOT}

%files -n %{name}-%{agent_web_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%{fe1appsdir}/%{servlet_agent_web}.war
%{fe1appsdir}/%{servlet_agent_web}/*

%files -n %{name}-%{agent_web_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%{fe2appsdir}/%{servlet_agent_web}.war
%{fe2appsdir}/%{servlet_agent_web}/*

%files -n %{name}-%{batch_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1batchdir}/lib
%dir %{fe1batchdir}/config
%dir %{fe1batchdir}/scenario
%dir %{fe1batchdir}/template/
%dir %{fe1batchdir}/perl5/
%{fe1batchdir}/lib/*
%{fe1batchdir}/config/*
%{fe1batchdir}/scenario/*
%{fe1batchdir}/template/*
%{fe1batchdir}/perl5/*

%files -n %{name}-%{batch_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2batchdir}/lib
%dir %{fe2batchdir}/config
%dir %{fe2batchdir}/scenario
%dir %{fe2batchdir}/template/
%dir %{fe2batchdir}/perl5/
%{fe2batchdir}/lib/*
%{fe2batchdir}/config/*
%{fe2batchdir}/scenario/*
%{fe2batchdir}/template/*
%{fe2batchdir}/perl5/*

%changelog
* Fri Nov 2 2018 tak-suzuki <tak-suzuki@jprs.co.jp>
- first release
