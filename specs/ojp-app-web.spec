# Conditional build
#

#
# rpmbuild -ba ~/rpm/SPECS/ojp-app-web.spec \
#              --define='version 20170919203743' \
#              --define='release PIW.019.REAL.REL'
#
%define account              dotjp1
%define account_group        dotjp1
%define world                real
%define app_agent_web        agent-web
%define app_internal_web     internal-web
%define tld                  ojp
%define servlet_agent_web    %{tld}-%{app_agent_web}
%define servlet_internal_web %{tld}-%{app_internal_web}
%define fe1                  f1
%define fe1basedir           /nfs/reg/data/%{fe1}/%{account}
%define fe1appsdir           %{fe1basedir}/servlet/webapps
%define fe1servletbindir     %{fe1basedir}/servlet/bin
%define fe1servletconfdir    %{fe1basedir}/servlet/conf
%define fe2                  f2
%define fe2basedir           /nfs/reg/data/%{fe2}/%{account}
%define fe2appsdir           %{fe2basedir}/servlet/webapps
%define fe2servletbindir     %{fe2basedir}/servlet/bin
%define fe2servletconfdir    %{fe2basedir}/servlet/conf
%define htdocs_world         tb-agent-web

%define agent_web_package    agent-web
%define internal_web_package internal-web
%define batch_package        batch

%define ojp_conf_app_agent_web     ojp-conf-agent-web
%define ojp_conf_app_agent_web_ver 20171108141728

%define debug_package %{nil}
%define __jar_repack %{nil}

%bcond_with branch

Summary:     ojp Registry System 
Summary(ja): ojp Registry System 
Name:        ojp-app-web
Version:     %{version}
Release:     %{release}
License:     Copyright(c) 2017 JPRS
Group:       Applications/Internet/Registry

%description
ojp Registry System

###
### ojp-app-web-agent-web
###
%package -n %{name}-%{agent_web_package}-%{fe1}
Summary:  ojp Registry System for f1
Group:    Applications/Internet/Registry
Requires: %{ojp_conf_app_agent_web}-%{fe1} >= %{ojp_conf_app_agent_web_ver}

%description -n %{name}-%{agent_web_package}-%{fe1}
ojp registry web system for f1

%package -n %{name}-%{agent_web_package}-%{fe2}
Summary:  ojp Registry System for f2
Group:    Applications/Internet/Registry
Requires: %{ojp_conf_app_agent_web}-%{fe2} >= %{ojp_conf_app_agent_web_ver}

%description -n %{name}-%{agent_web_package}-%{fe2}
ojp registry web system for f2

###
### ojp-app-web-internal-web
###
%package -n %{name}-%{internal_web_package}-%{fe1}
Summary:  ojp Registry Internal Web System for f1
Group:    Applications/Internet/Registry
###Requires: %{ojp_conf_app_internal_web}-%{fe1} >= %{ojp_conf_app_internal_web_ver}

%description -n %{name}-%{internal_web_package}-%{fe1}
ojp registry internal web system for f1

%package -n %{name}-%{internal_web_package}-%{fe2}
Summary:  ojp Registry Internal Web System for f2
Group:    Applications/Internet/Registry
###Requires: %{ojp_conf_app_internal_web}-%{fe2} >= %{ojp_conf_app_internal_web_ver}

%description -n %{name}-%{internal_web_package}-%{fe2}
ojp registry internal web system for f2

###
### ojp-app-web-batch
###
%package -n %{name}-%{batch_package}-%{fe1}
Summary:  ojp Registry Batch System for f1
Group:    Applications/Internet/Registry
###Requires: %{ojp_conf_app_batch}-%{fe1} >= %{ojp_conf_app_batch_ver}

%description -n %{name}-%{batch_package}-%{fe1}
ojp registry batch system for f1

%package -n %{name}-%{batch_package}-%{fe2}
Summary:  ojp Registry Batch System for f2
Group:    Applications/Internet/Registry
###Requires: %{ojp_conf_app_batch}-%{fe2} >= %{ojp_conf_app_batch_ver}

%description -n %{name}-%{batch_package}-%{fe2}
ojp registry batch system for f2

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
svn co --depth immediates http://svn1.jprs.co.jp/system/${TAG}/src/domain/registry-ojp ./src/domain/registry-ojp
svn co --depth immediates http://svn1.jprs.co.jp/release/trunk/dotjp-real/app/reg/data/f/dotjp1 ./release/dotjp1
svn up --set-depth infinity ./src/framework/jfk/WEB-INF
svn up --set-depth infinity ./src/framework/jfk/src
svn up --set-depth infinity ./src/domain/common/WEB-INF
svn up --set-depth infinity ./src/domain/common/src
svn up --set-depth infinity ./src/domain/registry-ojp/agent
svn up --set-depth infinity ./src/domain/registry-ojp/vendors
svn up --set-depth infinity ./src/domain/registry-ojp/image
svn up --set-depth infinity ./src/domain/registry-ojp/WEB-INF
svn up --set-depth infinity ./src/domain/registry-ojp/src
svn up --set-depth infinity ./src/domain/registry-ojp/css
svn up --set-depth infinity ./src/domain/registry-ojp/js
svn up --set-depth infinity ./release/dotjp1/servlet/bin
svn up --set-depth infinity ./release/dotjp1/servlet/conf

%build
export JAVA_HOME=/usr/local/jdk1.8/
cd ./src/domain/registry-ojp/
/usr/local/ant/bin/ant \
   -f build.domain.registry.ojp.xml \
   -Drelease.mode=product

%install
[ "${RPM_BUILD_ROOT}" != "/" ] && %__rm -rf ${RPM_BUILD_ROOT}

export JAR_BIN=/usr/local/jdk1.8/bin/jar

### ojp-agent-web
pushd ./src/domain/registry-ojp/build.war/build.agent.web
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}
%__install -p -m644 agent.php ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/
%__install -p -m644 agent.php ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF
%__install -p -m644 WEB-INF/web.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/config/
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb
%__install -p -m644 WEB-INF/config/agentweb/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/
%__install -p -m644 WEB-INF/config/agentweb/*.properties ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/data
%__install -p -m644 WEB-INF/data/*.txt ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/data/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/lib
%__install -p -m644 WEB-INF/lib/*.jar ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/lib/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script
%__install -p -m644 WEB-INF/script/*.xls ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/scenario
%__install -p -m644 WEB-INF/script/agentweb/*.xls ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/
%__install -p -m644 WEB-INF/script/agentweb/scenario/*.xls ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/scenario/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb
%__install -p -m644 WEB-INF/template/agentweb/*.html ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb/
%__install -p -m644 WEB-INF/template/agentweb/*.vm ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/template/ojprrpdao
%__install -p -m644 WEB-INF/template/ojprrpdao/*.txt ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/template/ojprrpdao/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image/agentweb/agent/menu
%__install -p -m644 image/agentweb/agent/menu/*.gif ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image/agentweb/agent/menu/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image/agentweb/agent/titleboard
%__install -p -m644 image/agentweb/agent/titleboard/*.gif ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image/agentweb/agent/titleboard/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image/agentweb/common
%__install -p -m644 image/agentweb/common/*.gif ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/image/agentweb/common/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/vendors/agentweb
%__install -p -m644 vendors/agentweb/*.js ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/vendors/agentweb/
%__install -p -m644 vendors/agentweb/*.css ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/vendors/agentweb/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/vendors/agentweb/images
%__install -p -m644 vendors/agentweb/images/*.png ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/vendors/agentweb/images/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/agent/apply/web
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/enums
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/file
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/local
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/download

%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/agent/apply/web/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/agent/apply/web/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/check/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/check/*.properties ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/enums/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/enums/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/util/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/file/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/file/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/local/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/local/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/download/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/download/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF
%__install -p -m644 WEB-INF/web.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/config/
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb
%__install -p -m644 WEB-INF/config/agentweb/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/
%__install -p -m644 WEB-INF/config/agentweb/*.properties ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/config/agentweb/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/data
%__install -p -m644 WEB-INF/data/*.txt ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/data/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/lib
%__install -p -m644 WEB-INF/lib/*.jar ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/lib/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script
%__install -p -m644 WEB-INF/script/*.xls ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/scenario
%__install -p -m644 WEB-INF/script/agentweb/*.xls ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/
%__install -p -m644 WEB-INF/script/agentweb/scenario/*.xls ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/script/agentweb/scenario/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb
%__install -p -m644 WEB-INF/template/agentweb/*.html ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb/
%__install -p -m644 WEB-INF/template/agentweb/*.vm ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/template/agentweb/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/template/ojprrpdao
%__install -p -m644 WEB-INF/template/ojprrpdao/*.txt ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/template/ojprrpdao/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image/agentweb/agent/menu
%__install -p -m644 image/agentweb/agent/menu/*.gif ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image/agentweb/agent/menu/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image/agentweb/agent/titleboard
%__install -p -m644 image/agentweb/agent/titleboard/*.gif ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image/agentweb/agent/titleboard/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image/agentweb/common
%__install -p -m644 image/agentweb/common/*.gif ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/image/agentweb/common/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/vendors/agentweb
%__install -p -m644 vendors/agentweb/*.js ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/vendors/agentweb/
%__install -p -m644 vendors/agentweb/*.css ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/vendors/agentweb/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/vendors/agentweb/images
%__install -p -m644 vendors/agentweb/images/*.png ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/vendors/agentweb/images/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/agent/apply/web
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/enums
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/file
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/local
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/download

%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/agent/apply/web/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/agent/apply/web/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/check/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/check/*.properties ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/enums/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/enums/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/util/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/file/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/file/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/local/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/local/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/download/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/download/

%__install -p -m644 dest/%{servlet_agent_web}.war ${RPM_BUILD_ROOT}%{fe1appsdir}
%__install -p -m644 dest/%{servlet_agent_web}.war ${RPM_BUILD_ROOT}%{fe2appsdir}

popd

### ojp-internal-web
pushd ./src/domain/registry-ojp/build.war/build.internal.web
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF
%__install -p -m644 WEB-INF/web.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/config/
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/config/internalweb
%__install -p -m644 WEB-INF/config/internalweb/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/config/internalweb/
%__install -p -m644 WEB-INF/config/internalweb/*.properties ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/config/internalweb/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/data
%__install -p -m644 WEB-INF/data/*.txt ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/data/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/lib
%__install -p -m644 WEB-INF/lib/*.jar ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/lib/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/script
%__install -p -m644 WEB-INF/script/*.xls ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/script/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/script/internalweb/scenario
%__install -p -m644 WEB-INF/script/internalweb/*.xls ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/script/internalweb/
%__install -p -m644 WEB-INF/script/internalweb/scenario/*.xls ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/script/internalweb/scenario/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb
%__install -p -m644 WEB-INF/template/internalweb/*.html ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb/
%__install -p -m644 WEB-INF/template/internalweb/*.vm ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb/
%__install -p -m644 WEB-INF/template/internalweb/*.jrxml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb/
%__install -p -m644 WEB-INF/template/internalweb/*.txt ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/template/ojprrpdao
%__install -p -m644 WEB-INF/template/ojprrpdao/*.txt ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/template/ojprrpdao/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb
%__install -p -m644 vendors/internalweb/*.js ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/
%__install -p -m644 vendors/internalweb/*.css ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/images
%__install -p -m644 vendors/internalweb/images/*.png ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/images/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/img
%__install -p -m644 vendors/internalweb/img/*.png ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/img/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18
%__install -p -m644 vendors/internalweb/dataTables-1.10.18/*.css ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18/
%__install -p -m644 vendors/internalweb/dataTables-1.10.18/*.js ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18/images
%__install -p -m644 vendors/internalweb/dataTables-1.10.18/images/*.png ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18/images/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/css/internalweb
%__install -p -m644 css/internalweb/*.css ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/css/internalweb/

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/js/internalweb

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/internal/business/web
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/enums
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/file
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/local
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/download

%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/internal/business/web/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/internal/business/web/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table/*.xml ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/check/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/check/*.properties ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/enums/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/enums/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/util/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/file/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/file/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/local/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/local/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/download/*.class ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/download/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF
%__install -p -m644 WEB-INF/web.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/config/
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/config/internalweb
%__install -p -m644 WEB-INF/config/internalweb/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/config/internalweb/
%__install -p -m644 WEB-INF/config/internalweb/*.properties ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/config/internalweb/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/data
%__install -p -m644 WEB-INF/data/*.txt ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/data/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/lib
%__install -p -m644 WEB-INF/lib/*.jar ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/lib/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/script
%__install -p -m644 WEB-INF/script/*.xls ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/script/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/script/internalweb/scenario
%__install -p -m644 WEB-INF/script/internalweb/*.xls ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/script/internalweb/
%__install -p -m644 WEB-INF/script/internalweb/scenario/*.xls ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/script/internalweb/scenario/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb
%__install -p -m644 WEB-INF/template/internalweb/*.html ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb/
%__install -p -m644 WEB-INF/template/internalweb/*.vm ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb/
%__install -p -m644 WEB-INF/template/internalweb/*.jrxml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb/
%__install -p -m644 WEB-INF/template/internalweb/*.txt ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/template/internalweb/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/template/ojprrpdao
%__install -p -m644 WEB-INF/template/ojprrpdao/*.txt ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/template/ojprrpdao/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb
%__install -p -m644 vendors/internalweb/*.js ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/
%__install -p -m644 vendors/internalweb/*.css ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/images
%__install -p -m644 vendors/internalweb/images/*.png ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/images/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/img
%__install -p -m644 vendors/internalweb/img/*.png ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/img/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18
%__install -p -m644 vendors/internalweb/dataTables-1.10.18/*.css ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18/
%__install -p -m644 vendors/internalweb/dataTables-1.10.18/*.js ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18/images
%__install -p -m644 vendors/internalweb/dataTables-1.10.18/images/*.png ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/vendors/internalweb/dataTables-1.10.18/images/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/css/internalweb
%__install -p -m644 css/internalweb/*.css ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/css/internalweb/

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/js/internalweb

%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/internal/business/web
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/enums
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/file
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/local
%__install -d ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/download

%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/internal/business/web/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/internal/business/web/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/authgamen/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/generalmaster/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/constant/prefecture/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/dojp/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domain/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/domalloc/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/ojpspool/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/person/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/logical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/physical/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table/*.xml ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/db/tie/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/reader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/uploader/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/file/writer/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dao/rrp/ojp/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/dojp/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domain/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/domalloc/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/ojpspool/view/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/person/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/regif/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/join/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/db/tie/table/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/mail/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/integration/dto/xml/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/check/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/check/*.properties ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/check/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/enums/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/enums/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/util/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/util/batch/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/library/web/thread/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/file/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/file/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/common/model/local/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/common/model/local/
%__install -p -m644 classes/jp/co/jprs/domain/registry/ojp/download/*.class ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/WEB-INF/classes/jp/co/jprs/domain/registry/ojp/download/

popd

### batch
pushd ./src/domain/registry-ojp/build.war/build.batch
%__install -d ${RPM_BUILD_ROOT}%{fe1basedir}/config
%__install -p -m644 config/*.xml ${RPM_BUILD_ROOT}%{fe1basedir}/config/
%__install -p -m644 config/*.properties ${RPM_BUILD_ROOT}%{fe1basedir}/config/
%__install -p -m644 config/*.dtd ${RPM_BUILD_ROOT}%{fe1basedir}/config/
%__install -d ${RPM_BUILD_ROOT}%{fe1basedir}/lib
%__install -p -m644 lib/*.jar ${RPM_BUILD_ROOT}%{fe1basedir}/lib/
%__install -d ${RPM_BUILD_ROOT}%{fe1basedir}/scenario/job
%__install -d ${RPM_BUILD_ROOT}%{fe1basedir}/scenario/job/config
%__install -p -m755 scenario/job/*.sh ${RPM_BUILD_ROOT}%{fe1basedir}/scenario/job/
%__install -p -m644 scenario/job/config/*.conf ${RPM_BUILD_ROOT}%{fe1basedir}/scenario/job/config/
%__install -d ${RPM_BUILD_ROOT}%{fe1basedir}/template
%__install -p -m644 template/*.txt ${RPM_BUILD_ROOT}%{fe1basedir}/template/

%__install -d ${RPM_BUILD_ROOT}%{fe2basedir}/config
%__install -p -m644 config/*.xml ${RPM_BUILD_ROOT}%{fe2basedir}/config/
%__install -p -m644 config/*.properties ${RPM_BUILD_ROOT}%{fe2basedir}/config/
%__install -p -m644 config/*.dtd ${RPM_BUILD_ROOT}%{fe2basedir}/config/
%__install -d ${RPM_BUILD_ROOT}%{fe2basedir}/lib
%__install -p -m644 lib/*.jar ${RPM_BUILD_ROOT}%{fe2basedir}/lib/
%__install -d ${RPM_BUILD_ROOT}%{fe2basedir}/scenario/job
%__install -d ${RPM_BUILD_ROOT}%{fe2basedir}/scenario/job/config
%__install -p -m755 scenario/job/*.sh ${RPM_BUILD_ROOT}%{fe2basedir}/scenario/job/
%__install -p -m644 scenario/job/config/*.conf ${RPM_BUILD_ROOT}%{fe2basedir}/scenario/job/config/
%__install -d ${RPM_BUILD_ROOT}%{fe2basedir}/template
%__install -p -m644 template/*.txt ${RPM_BUILD_ROOT}%{fe2basedir}/template/
popd

pushd ./release/dotjp1

%__install -d ${RPM_BUILD_ROOT}%{fe1servletbindir}
%__install -d ${RPM_BUILD_ROOT}%{fe1servletconfdir}

%__install -p -m755 servlet/bin/*.sh ${RPM_BUILD_ROOT}%{fe1servletbindir}
%__install -p -m644 servlet/conf/*.policy ${RPM_BUILD_ROOT}%{fe1servletconfdir}
%__install -p -m644 servlet/conf/*.properties ${RPM_BUILD_ROOT}%{fe1servletconfdir}
%__install -p -m644 servlet/conf/*.xml ${RPM_BUILD_ROOT}%{fe1servletconfdir}

%__install -d ${RPM_BUILD_ROOT}%{fe2servletbindir}
%__install -d ${RPM_BUILD_ROOT}%{fe2servletconfdir}

%__install -p -m755 servlet/bin/*.sh ${RPM_BUILD_ROOT}%{fe2servletbindir}
%__install -p -m644 servlet/conf/*.policy ${RPM_BUILD_ROOT}%{fe2servletconfdir}
%__install -p -m644 servlet/conf/*.properties ${RPM_BUILD_ROOT}%{fe2servletconfdir}
%__install -p -m644 servlet/conf/*.xml ${RPM_BUILD_ROOT}%{fe2servletconfdir}

popd

%__mkdir_p ${RPM_BUILD_ROOT}%{fe1basedir}/%{app_agent_web}/htdocs
%__mkdir_p ${RPM_BUILD_ROOT}%{fe2basedir}/%{app_agent_web}/htdocs
%__mkdir_p ${RPM_BUILD_ROOT}%{fe1basedir}/%{htdocs_world}/htdocs
%__mkdir_p ${RPM_BUILD_ROOT}%{fe2basedir}/%{htdocs_world}/htdocs
%__ln_s /logs/dotjp1/tomcat ${RPM_BUILD_ROOT}%{fe1basedir}/servlet/logs
%__ln_s /local/dotjp1/servlet/tomcat/temp ${RPM_BUILD_ROOT}%{fe1basedir}/servlet/temp
%__ln_s /local/dotjp1/servlet/tomcat/var ${RPM_BUILD_ROOT}%{fe1basedir}/servlet/var
%__ln_s /local/dotjp1/servlet/tomcat/work ${RPM_BUILD_ROOT}%{fe1basedir}/servlet/work
%__ln_s /logs/dotjp1/tomcat ${RPM_BUILD_ROOT}%{fe2basedir}/servlet/logs
%__ln_s /local/dotjp1/servlet/tomcat/temp ${RPM_BUILD_ROOT}%{fe2basedir}/servlet/temp
%__ln_s /local/dotjp1/servlet/tomcat/var ${RPM_BUILD_ROOT}%{fe2basedir}/servlet/var
%__ln_s /local/dotjp1/servlet/tomcat/work ${RPM_BUILD_ROOT}%{fe2basedir}/servlet/work

%pre -n %{name}-%{agent_web_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_agent_web}/*

%pre -n %{name}-%{agent_web_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_agent_web}/*

%pre -n %{name}-%{internal_web_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internal_web}/*

%pre -n %{name}-%{internal_web_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internal_web}/*

%pre -n %{name}-%{batch_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/lib/*
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/scenario/*

%pre -n %{name}-%{batch_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/lib/*
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/scenario/*

%clean
%__rm -rf ${RPM_BUILD_ROOT}

%files -n %{name}-%{agent_web_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1appsdir}
%dir %{fe1appsdir}/%{servlet_agent_web}
%dir %{fe1basedir}/%{app_agent_web}
%dir %{fe1basedir}/%{app_agent_web}/htdocs
%dir %{fe1basedir}/%{htdocs_world}
%dir %{fe1basedir}/%{htdocs_world}/htdocs
%dir %{fe1servletbindir}
%{fe1servletbindir}/*.sh
%dir %{fe1servletconfdir}
%{fe1servletconfdir}/*.policy
%{fe1servletconfdir}/*.properties
%{fe1servletconfdir}/*.xml
%{fe1basedir}/servlet/logs
%{fe1basedir}/servlet/temp
%{fe1basedir}/servlet/var
%{fe1basedir}/servlet/work
%{fe1appsdir}/%{servlet_agent_web}.war
%{fe1appsdir}/%{servlet_agent_web}/*

%files -n %{name}-%{agent_web_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2appsdir}
%dir %{fe2appsdir}/%{servlet_agent_web}
%dir %{fe2basedir}/%{app_agent_web}
%dir %{fe2basedir}/%{app_agent_web}/htdocs
%dir %{fe2basedir}/%{htdocs_world}
%dir %{fe2basedir}/%{htdocs_world}/htdocs
%dir %{fe2servletbindir}
%{fe2servletbindir}/*.sh
%dir %{fe2servletconfdir}
%{fe2servletconfdir}/*.policy
%{fe2servletconfdir}/*.properties
%{fe2servletconfdir}/*.xml
%{fe2basedir}/servlet/logs
%{fe2basedir}/servlet/temp
%{fe2basedir}/servlet/var
%{fe2basedir}/servlet/work
%{fe2appsdir}/%{servlet_agent_web}.war
%{fe2appsdir}/%{servlet_agent_web}/*

%files -n %{name}-%{internal_web_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1appsdir}/%{servlet_internal_web}
%{fe1appsdir}/%{servlet_internal_web}/*

%files -n %{name}-%{internal_web_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2appsdir}/%{servlet_internal_web}
%{fe2appsdir}/%{servlet_internal_web}/*

%files -n %{name}-%{batch_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1basedir}/lib
%dir %{fe1basedir}/config
%dir %{fe1basedir}/scenario
%dir %{fe1basedir}/template/
%{fe1basedir}/lib/*
%{fe1basedir}/config/*
%{fe1basedir}/scenario/*
%{fe1basedir}/template/*

%files -n %{name}-%{batch_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2basedir}/lib
%dir %{fe2basedir}/config
%dir %{fe2basedir}/scenario/
%dir %{fe2basedir}/template/
%{fe2basedir}/lib/*
%{fe2basedir}/config/*
%{fe2basedir}/scenario/*
%{fe2basedir}/template/*

%changelog
* Tue Jul 28 2020 n-tanaka <n-tanaka@jprs.co.jp>
- Add New Java Package 

* Mon Aug 27 2018 n-tanaka <n-tanaka@jprs.co.jp>
- Add Internal Web and Batch System

* Tue Apr 3 2018 t-sakuma <t-sakuma@jprs.co.jp>
Fixed package definitions [JPRS sysreq-staff 40616]

* Tue Sep 26 2017 t-sakuma <t-sakuma@jprs.co.jp>
- first release
