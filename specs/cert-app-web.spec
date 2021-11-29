# Conditional build
#

#
# rpmbuild -ba ~/rpm/SPECS/cert-app-web.spec \
#              --define='version 20170919203743' \
#              --define='release PIW.019.REAL.REL'
#

%define account           app000
%define account_group     app000
%define world             real
%define apply             apply
%define internal          internal
%define bootstrap         bootstrap
%define system_name       certmanager
%define servlet_apply     %{system_name}-%{apply}
%define servlet_bootstrap %{system_name}-%{bootstrap}
%define servlet_internal  %{system_name}-%{internal}
%define base_dir          /data/app001
%define webapps_dir       %{base_dir}/webapps
%define apply_dir         %{webapps_dir}/%{servlet_apply}
%define bootstrap_dir     %{webapps_dir}/%{servlet_bootstrap}
%define internal_dir      %{webapps_dir}/%{servlet_internal}
%define apply_ver         20190404105410
%define bootstrap_ver     20190404105410

%define debug_package %{nil}
%define __jar_repack  %{nil}

%bcond_with branch
%bcond_with real

%if %{with real}
%define environment real
%else
%define environment jail
%endif

####################################
## 証明書管理I/Fパッケージ基本情報
####################################
Summary:     Certificate Management System
Summary(ja): 証明書管理I/F
Name:        cert-app-web
Version:     %{version}
Release:     %{release}.%{environment}
License:     Copyright(c) JPRS
Group:       Applications/Internet/Cert

%description
Certificate Management System

####################################
## cert-apply package info
####################################
%package -n %{name}-%{apply}
Summary:  Certificate Management System Apply
Group:    Applications/Internet/Cert

%description -n %{name}-%{apply}
Certificate Management System Apply

####################################
## cert-bootstrap package info
####################################
%package -n %{name}-%{bootstrap}
Summary:  Certificate Management System Bootstrap
Group:    Applications/Internet/Cert

%description -n %{name}-%{bootstrap}
Certificate Management System Bootstrap

####################################
## cert-internal package info
####################################
%package -n %{name}-%{internal}
Summary:  Certificate Management System Internal
Group:    Applications/Internet/Cert
Requires: %{name}-%{apply} >= %{apply_ver}
Requires: %{name}-%{bootstrap} >= %{bootstrap_ver}

%description -n %{name}-%{internal}
Certificate Management System Internal

%prep

%setup -T -c %{name}-%{version}

REL=`echo %{release} | %__sed -e 's/\.%{environment}$//g'`
%if %{with branch}
TAG=`echo ${REL} | %__sed -e 's/\./-/g'`
if [ ${REL} != "trunk" ]; then
    TAG="branches/${TAG}"
fi
%else
    TAG="tags/"`echo ${REL}-%{version} | %__sed -e 's/\./-/g'`
%endif

svn co http://svn1.jprs.co.jp/system/${TAG}/src/cert/agent/ ./src/cert/agent

%build
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk/
cd ./src/cert/agent/buildroot

%if %{with real}
    TNAME="prod-tyo"
%else
    TNAME="jail"
%endif

/usr/local/ant/bin/ant \
  -f build.xml \
  -Dtarget_world=${TNAME} \
  build-all

%install
[ "${RPM_BUILD_ROOT}" != "/" ] && %__rm -rf ${RPM_BUILD_ROOT}

export JAR_BIN=/usr/lib/jvm/java-1.8.0-openjdk/bin/jar


####################################
## cert-apply install section
####################################
pushd ./src/cert/agent/buildroot/webroot/%{servlet_apply}
%__install -d ${RPM_BUILD_ROOT}%{webapps_dir}
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}
%__install -d ${RPM_BUILD_ROOT}%{base_dir}/htdocs

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF
%__install -p -m644 WEB-INF/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/
%__install -p -m644 WEB-INF/velocity.properties ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/
%__install -p -m644 WEB-INF/VM_global_library.vm ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/lib
%__install -p -m644 WEB-INF/lib/*.jar ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/lib/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes
%__install -p -m644 WEB-INF/classes/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/
%__install -p -m644 WEB-INF/classes/*.properties ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/
%__install -p -m644 WEB-INF/classes/*.dicon ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/org/apache/velocity/runtime/parser/node
%__install -p -m644 WEB-INF/classes/org/apache/velocity/runtime/parser/node/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/org/apache/velocity/runtime/parser/node/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/org/seasar/xwork2
%__install -p -m644 WEB-INF/classes/org/seasar/xwork2/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/org/seasar/xwork2/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/org/seasar/xwork2/component
%__install -p -m644 WEB-INF/classes/org/seasar/xwork2/component/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/org/seasar/xwork2/component/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/addadmin
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/addoperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/deleteadminandoperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/home
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/inquiryinformation
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/login
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/reissuecertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/updatecertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/updateinformation
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/updatepassword
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dao/common
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dicon
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/addadmin
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/addoperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/common
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/deleteadminandoperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/home
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/inquiryinformation
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/login
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/reissuecertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/updatecertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/updateinformation
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/updatepassword
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/interceptor
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/addadmin
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/addoperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/deleteadminandoperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/home
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/inquiryinformation
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/reissuecertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/updatecertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/updateinformation
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/updatepassword

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/package.properties ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/addadmin/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/addadmin/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/addoperator/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/addoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/deleteadminandoperator/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/deleteadminandoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/home/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/home/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/inquiryinformation/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/inquiryinformation/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/login/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/login/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/reissuecertificate/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/reissuecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/updatecertificate/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/updatecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/updateinformation/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/updateinformation/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/updatepassword/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/action/updatepassword/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dao/common/LoginInfoDao.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dao/common/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dicon/dev.dicon ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dicon/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/addadmin/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/addadmin/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/addoperator/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/addoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/common/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/common/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/deleteadminandoperator/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/deleteadminandoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/home/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/home/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/inquiryinformation/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/inquiryinformation/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/login/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/login/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/reissuecertificate/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/reissuecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/updatecertificate/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/updatecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/updateinformation/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/updateinformation/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/updatepassword/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/dto/updatepassword/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/interceptor/LoginInterceptor.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/interceptor/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/addadmin/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/addadmin/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/addoperator/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/addoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/deleteadminandoperator/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/deleteadminandoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/home/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/home/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/inquiryinformation/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/inquiryinformation/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/reissuecertificate/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/reissuecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/updatecertificate/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/updatecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/updateinformation/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/updateinformation/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/updatepassword/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{apply}/logic/updatepassword/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/action
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/base
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dicon
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/agentinfo
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authscreen
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authuser
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfo
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfohistory
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/limitlicense
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/maintenanceinfo
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/unregistereduser
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfo
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfohistory
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/mail
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/entity
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/dao
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/exception
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/filter
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/interceptor
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/log
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/string
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/validator

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/action/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/action/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/base/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/base/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dicon/*.dicon ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dicon/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/agentinfo/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/agentinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authscreen/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authscreen/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authuser/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authuser/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfo/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfohistory/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfohistory/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/limitlicense/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/limitlicense/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/maintenanceinfo/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/maintenanceinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/unregistereduser/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/unregistereduser/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfo/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfohistory/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfohistory/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/mail/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/mail/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/entity/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/entity/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/dao/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/dao/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/exception/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/exception/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/filter/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/filter/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/interceptor/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/interceptor/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/log/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/log/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/string/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/string/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/validator/*.class  ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/validator/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/interceptor
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/interceptor/*.class ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/interceptor/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/addAdmin
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/addOperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/deleteAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/reissueCertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/updateCertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/updateInformation
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/updatePassword
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/bootstrap
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/bootstrap/acceptAdmin
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/bootstrap/activateAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/bootstrap/issueOTU
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/internal
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/internal/internalDeleteAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/internal/internalReissueCertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/internal/registAdmin
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/internal/registMaintenance

%__install -p -m644 WEB-INF/mail/apply/addAdmin/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/addAdmin/
%__install -p -m644 WEB-INF/mail/apply/addOperator/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/addOperator/
%__install -p -m644 WEB-INF/mail/apply/deleteAdminAndOperator/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/deleteAdminAndOperator/
%__install -p -m644 WEB-INF/mail/apply/reissueCertificate/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/reissueCertificate/
%__install -p -m644 WEB-INF/mail/apply/updateCertificate/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/updateCertificate/
%__install -p -m644 WEB-INF/mail/apply/updateInformation/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/updateInformation/
%__install -p -m644 WEB-INF/mail/apply/updatePassword/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/apply/updatePassword/

%__install -p -m644 WEB-INF/mail/bootstrap/acceptAdmin/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/bootstrap/acceptAdmin/
%__install -p -m644 WEB-INF/mail/bootstrap/activateAdminAndOperator/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/bootstrap/activateAdminAndOperator/
%__install -p -m644 WEB-INF/mail/bootstrap/issueOTU/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/bootstrap/issueOTU/

%__install -p -m644 WEB-INF/mail/internal/internalDeleteAdminAndOperator/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/internal/internalDeleteAdminAndOperator/
%__install -p -m644 WEB-INF/mail/internal/internalReissueCertificate/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/internal/internalReissueCertificate/
%__install -p -m644 WEB-INF/mail/internal/registAdmin/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/internal/registAdmin/
%__install -p -m644 WEB-INF/mail/internal/registMaintenance/*.xml ${RPM_BUILD_ROOT}%{apply_dir}/WEB-INF/mail/internal/registMaintenance/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/common/css
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/common/img
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/common/js

%__install -p -m644 ui/common/css/*.css ${RPM_BUILD_ROOT}%{apply_dir}/ui/common/css/
%__install -p -m644 ui/common/img/*.gif ${RPM_BUILD_ROOT}%{apply_dir}/ui/common/img/
%__install -p -m644 ui/common/js/*.js ${RPM_BUILD_ROOT}%{apply_dir}/ui/common/js/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap-admin-theme/assets
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap-datepicker/css
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap-datepicker/js
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap-datepicker/locales
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap/css
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap/img
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap/js
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/css
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/css
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/images
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/images/psd
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/js
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/swf
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/images
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/js
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/js

%__install -p -m644 ui/vendors/bootstrap-admin-theme/assets/*.css ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap-admin-theme/assets/
%__install -p -m644 ui/vendors/bootstrap-admin-theme/assets/*.js ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap-admin-theme/assets/

%__install -p -m644 ui/vendors/bootstrap-datepicker/css/*.css ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap-datepicker/css/
%__install -p -m644 ui/vendors/bootstrap-datepicker/js/*.js ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap-datepicker/js/
%__install -p -m644 ui/vendors/bootstrap-datepicker/locales/*.js ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap-datepicker/locales/

%__install -p -m644 ui/vendors/bootstrap/css/*.css ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap/css/
%__install -p -m644 ui/vendors/bootstrap/img/Thumbs.db ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap/img/
%__install -p -m644 ui/vendors/bootstrap/img/*.png ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap/img/
%__install -p -m644 ui/vendors/bootstrap/js/*.js ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/bootstrap/js/

%__install -p -m644 ui/vendors/datatables/css/*.css ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/css/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/css/*.css ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/css/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/images/*.png ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/images/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/images/psd/*.psd ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/images/psd/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/js/*.js ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/js/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/swf/*.swf ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/extras/tabletools/swf/
%__install -p -m644 ui/vendors/datatables/images/*.png ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/images/
%__install -p -m644 ui/vendors/datatables/js/*.js ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/js/
%__install -p -m644 ui/vendors/datatables/js/*.txt ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/datatables/js/

%__install -p -m644 ui/vendors/js/*.js ${RPM_BUILD_ROOT}%{apply_dir}/ui/vendors/js/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/addAdmin
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/addOperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/deleteAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/home
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/inquiryInformation
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/login
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/reissueCertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/updateCertificate
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/updateInformation
%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/updatePassword

%__install -p -m644 ui/view/%{apply}/addAdmin/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/addAdmin/
%__install -p -m644 ui/view/%{apply}/addOperator/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/addOperator/
%__install -p -m644 ui/view/%{apply}/deleteAdminAndOperator/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/deleteAdminAndOperator/
%__install -p -m644 ui/view/%{apply}/home/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/home/
%__install -p -m644 ui/view/%{apply}/inquiryInformation/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/inquiryInformation/
%__install -p -m644 ui/view/%{apply}/login/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/login/
%__install -p -m644 ui/view/%{apply}/reissueCertificate/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/reissueCertificate/
%__install -p -m644 ui/view/%{apply}/updateCertificate/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/updateCertificate/
%__install -p -m644 ui/view/%{apply}/updateInformation/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/updateInformation/
%__install -p -m644 ui/view/%{apply}/updatePassword/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/%{apply}/updatePassword/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/common
%__install -p -m644 ui/view/common/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/common/

%__install -d ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/systemError
%__install -p -m644 ui/view/systemError/*.vm ${RPM_BUILD_ROOT}%{apply_dir}/ui/view/systemError/

popd

####################################
## cert-bootstrap install section
####################################
pushd ./src/cert/agent/buildroot/webroot/%{servlet_bootstrap}
%__install -d ${RPM_BUILD_ROOT}%{webapps_dir}
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}
%__install -d ${RPM_BUILD_ROOT}%{base_dir}/htdocs

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF
%__install -p -m644 WEB-INF/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/
%__install -p -m644 WEB-INF/velocity.properties ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/
%__install -p -m644 WEB-INF/VM_global_library.vm ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/lib
%__install -p -m644 WEB-INF/lib/*.jar ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/lib/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes
%__install -p -m644 WEB-INF/classes/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/
%__install -p -m644 WEB-INF/classes/*.properties ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/
%__install -p -m644 WEB-INF/classes/*.dicon ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/org/apache/velocity/runtime/parser/node
%__install -p -m644 WEB-INF/classes/org/apache/velocity/runtime/parser/node/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/org/apache/velocity/runtime/parser/node/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/org/seasar/xwork2
%__install -p -m644 WEB-INF/classes/org/seasar/xwork2/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/org/seasar/xwork2/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/org/seasar/xwork2/component
%__install -p -m644 WEB-INF/classes/org/seasar/xwork2/component/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/org/seasar/xwork2/component/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/acceptadmin
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/activateadminandoperator
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/issueotu

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/package.properties ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/acceptadmin/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/acceptadmin/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/activateadminandoperator/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/activateadminandoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/issueotu/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/action/issueotu/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dicon
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dicon/dev.dicon ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dicon/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dto/acceptadmin
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dto/activateadminandoperator
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dto/issueotu

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dto/acceptadmin/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dto/acceptadmin/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dto/activateadminandoperator/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dto/activateadminandoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dto/issueotu/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/dto/issueotu/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/logic/acceptadmin
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/logic/activateadminandoperator
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/logic/issueotu

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/logic/acceptadmin/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/logic/acceptadmin/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/logic/activateadminandoperator/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/logic/activateadminandoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/logic/issueotu/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{bootstrap}/logic/issueotu/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/action
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/base
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dicon
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/agentinfo
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authscreen
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authuser
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfo
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfohistory
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/limitlicense
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/maintenanceinfo
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/unregistereduser
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfo
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfohistory
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/mail
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/entity
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/dao
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/exception
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/filter
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/interceptor
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/log
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/string
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/validator

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/action/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/action/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/base/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/base/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dicon/*.dicon ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dicon/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/agentinfo/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/agentinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authscreen/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authscreen/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authuser/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authuser/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfo/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfohistory/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfohistory/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/limitlicense/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/limitlicense/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/maintenanceinfo/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/maintenanceinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/unregistereduser/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/unregistereduser/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfo/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfohistory/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfohistory/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/mail/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/mail/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/entity/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/entity/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/dao/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/dao/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/exception/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/exception/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/filter/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/filter/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/interceptor/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/interceptor/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/log/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/log/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/string/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/string/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/validator/*.class  ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/validator/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/interceptor
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/interceptor/*.class ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/interceptor/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/addAdmin
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/addOperator
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/deleteAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/reissueCertificate
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/updateCertificate
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/updateInformation
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/updatePassword
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/bootstrap
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/bootstrap/acceptAdmin
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/bootstrap/activateAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/bootstrap/issueOTU
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/internal
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/internal/internalDeleteAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/internal/internalReissueCertificate
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/internal/registAdmin
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/internal/registMaintenance

%__install -p -m644 WEB-INF/mail/apply/addAdmin/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/addAdmin/
%__install -p -m644 WEB-INF/mail/apply/addOperator/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/addOperator/
%__install -p -m644 WEB-INF/mail/apply/deleteAdminAndOperator/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/deleteAdminAndOperator/
%__install -p -m644 WEB-INF/mail/apply/reissueCertificate/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/reissueCertificate/
%__install -p -m644 WEB-INF/mail/apply/updateCertificate/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/updateCertificate/
%__install -p -m644 WEB-INF/mail/apply/updateInformation/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/updateInformation/
%__install -p -m644 WEB-INF/mail/apply/updatePassword/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/apply/updatePassword/

%__install -p -m644 WEB-INF/mail/bootstrap/acceptAdmin/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/bootstrap/acceptAdmin/
%__install -p -m644 WEB-INF/mail/bootstrap/activateAdminAndOperator/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/bootstrap/activateAdminAndOperator/
%__install -p -m644 WEB-INF/mail/bootstrap/issueOTU/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/bootstrap/issueOTU/

%__install -p -m644 WEB-INF/mail/internal/internalDeleteAdminAndOperator/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/internal/internalDeleteAdminAndOperator/
%__install -p -m644 WEB-INF/mail/internal/internalReissueCertificate/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/internal/internalReissueCertificate/
%__install -p -m644 WEB-INF/mail/internal/registAdmin/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/internal/registAdmin/
%__install -p -m644 WEB-INF/mail/internal/registMaintenance/*.xml ${RPM_BUILD_ROOT}%{bootstrap_dir}/WEB-INF/mail/internal/registMaintenance/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/common/css
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/common/img
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/common/js

%__install -p -m644 ui/common/css/*.css ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/common/css/
%__install -p -m644 ui/common/img/*.gif ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/common/img/
%__install -p -m644 ui/common/js/*.js ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/common/js/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap-admin-theme/assets
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap-datepicker/css
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap-datepicker/js
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap-datepicker/locales
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap/css
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap/img
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap/js
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/css
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/css
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/images
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/images/psd
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/js
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/swf
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/images
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/js
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/js

%__install -p -m644 ui/vendors/bootstrap-admin-theme/assets/*.css ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap-admin-theme/assets/
%__install -p -m644 ui/vendors/bootstrap-admin-theme/assets/*.js ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap-admin-theme/assets/

%__install -p -m644 ui/vendors/bootstrap-datepicker/css/*.css ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap-datepicker/css/
%__install -p -m644 ui/vendors/bootstrap-datepicker/js/*.js ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap-datepicker/js/
%__install -p -m644 ui/vendors/bootstrap-datepicker/locales/*.js ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap-datepicker/locales/

%__install -p -m644 ui/vendors/bootstrap/css/*.css ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap/css/
%__install -p -m644 ui/vendors/bootstrap/img/Thumbs.db ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap/img/
%__install -p -m644 ui/vendors/bootstrap/img/*.png ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap/img/
%__install -p -m644 ui/vendors/bootstrap/js/*.js ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/bootstrap/js/

%__install -p -m644 ui/vendors/datatables/css/*.css ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/css/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/css/*.css ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/css/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/images/*.png ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/images/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/images/psd/*.psd ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/images/psd/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/js/*.js ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/js/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/swf/*.swf ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/extras/tabletools/swf/
%__install -p -m644 ui/vendors/datatables/images/*.png ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/images/
%__install -p -m644 ui/vendors/datatables/js/*.js ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/js/
%__install -p -m644 ui/vendors/datatables/js/*.txt ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/datatables/js/

%__install -p -m644 ui/vendors/js/*.js ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/vendors/js/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/%{bootstrap}/acceptAdmin
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/%{bootstrap}/activateAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/%{bootstrap}/issueOTU

%__install -p -m644 ui/view/%{bootstrap}/acceptAdmin/*.vm ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/%{bootstrap}/acceptAdmin/
%__install -p -m644 ui/view/%{bootstrap}/activateAdminAndOperator/*.vm ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/%{bootstrap}/activateAdminAndOperator/
%__install -p -m644 ui/view/%{bootstrap}/issueOTU/*.vm ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/%{bootstrap}/issueOTU/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/common
%__install -p -m644 ui/view/common/*.vm ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/common/

%__install -d ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/systemError
%__install -p -m644 ui/view/systemError/*.vm ${RPM_BUILD_ROOT}%{bootstrap_dir}/ui/view/systemError/

popd

####################################
## cert-internal install section
####################################
pushd ./src/cert/agent/buildroot/webroot/%{servlet_internal}
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}
%__install -d ${RPM_BUILD_ROOT}%{base_dir}/htdocs

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF
%__install -p -m644 WEB-INF/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/
%__install -p -m644 WEB-INF/velocity.properties ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/
%__install -p -m644 WEB-INF/VM_global_library.vm ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/lib
%__install -p -m644 WEB-INF/lib/*.jar ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/lib/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes
%__install -p -m644 WEB-INF/classes/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/
%__install -p -m644 WEB-INF/classes/*.properties ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/
%__install -p -m644 WEB-INF/classes/*.dicon ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/org/apache/velocity/runtime/parser/node
%__install -p -m644 WEB-INF/classes/org/apache/velocity/runtime/parser/node/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/org/apache/velocity/runtime/parser/node/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/org/seasar/xwork2
%__install -p -m644 WEB-INF/classes/org/seasar/xwork2/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/org/seasar/xwork2/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/org/seasar/xwork2/component
%__install -p -m644 WEB-INF/classes/org/seasar/xwork2/component/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/org/seasar/xwork2/component/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/adminAndOperatorInformationOutput
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalIndex
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internaldeleteadminandoperator
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalhome
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalinquiryinformation
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalreissuecertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/limitlicense
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/mailTemplateReference
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/managecertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/registadmin
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/unregisteredadmincancel
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/unregisteredadminlist
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/accountlockcancel
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/registmaintenance

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/package.properties ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/adminAndOperatorInformationOutput/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/adminAndOperatorInformationOutput/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalIndex/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalIndex/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internaldeleteadminandoperator/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internaldeleteadminandoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalhome/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalhome/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalinquiryinformation/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalinquiryinformation/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalreissuecertificate/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/internalreissuecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/limitlicense/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/limitlicense/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/mailTemplateReference/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/mailTemplateReference/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/managecertificate/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/managecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/registadmin/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/registadmin/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/unregisteredadmincancel/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/unregisteredadmincancel/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/unregisteredadminlist/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/unregisteredadminlist/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/accountlockcancel/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/accountlockcancel/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/registmaintenance/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/action/registmaintenance/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dicon
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dicon/dev.dicon ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dicon/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/common
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internaldeleteadminandoperator
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internalhome
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internalinquiryinformation
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internalreissuecertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/limitlicense
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/mailTemplateReference
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/mailTemplateReferenceList
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/managecertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/registadmin
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/unregisteredadminlist
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/registmaintenance

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/common/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/common/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internaldeleteadminandoperator/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internaldeleteadminandoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internalhome/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internalhome/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internalinquiryinformation/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internalinquiryinformation/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internalreissuecertificate/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/internalreissuecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/limitlicense/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/limitlicense/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/mailTemplateReference/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/mailTemplateReference/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/mailTemplateReferenceList/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/mailTemplateReferenceList/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/managecertificate/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/managecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/registadmin/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/registadmin/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/unregisteredadminlist/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/unregisteredadminlist/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/registmaintenance/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/dto/registmaintenance/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/interceptor
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/interceptor/InternalLoginInterceptor.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/interceptor/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/adminAndOperatorInformationOutput
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internaldeleteadminandoperator
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internalhome
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internalinquiryinformation
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internalreissuecertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/limitlicense
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/mailTemplateReference
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/registadmin
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/unregisteredadmincancel
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/unregisteredadminlist
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/accountlockcancel
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/registmaintenance

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/adminAndOperatorInformationOutput/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/adminAndOperatorInformationOutput/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internaldeleteadminandoperator/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internaldeleteadminandoperator/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internalhome/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internalhome/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internalinquiryinformation/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internalinquiryinformation/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internalreissuecertificate/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/internalreissuecertificate/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/limitlicense/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/limitlicense/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/mailTemplateReference/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/mailTemplateReference/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/registadmin/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/registadmin/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/unregisteredadmincancel/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/unregisteredadmincancel/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/unregisteredadminlist/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/unregisteredadminlist/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/accountlockcancel/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/accountlockcancel/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/registmaintenance/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/%{internal}/logic/registmaintenance/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/action
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/base
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dicon
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/agentinfo
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authscreen
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authuser
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfo
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfohistory
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/limitlicense
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/maintenanceinfo
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/unregistereduser
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfo
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfohistory
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/mail
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/entity
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/dao
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/exception
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/filter
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/interceptor
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/log
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/string
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/validator

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/action/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/action/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/base/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dao/base/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dicon/*.dicon ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dicon/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/agentinfo/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/agentinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authscreen/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authscreen/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authuser/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/authuser/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfo/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfohistory/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/certificateinfohistory/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/limitlicense/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/limitlicense/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/maintenanceinfo/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/maintenanceinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/unregistereduser/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/unregistereduser/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfo/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfo/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfohistory/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/base/userinfohistory/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/mail/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/dto/mail/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/entity/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/entity/

%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/dao/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/dao/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/exception/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/exception/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/filter/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/filter/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/interceptor/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/interceptor/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/log/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/log/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/string/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/string/
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/validator/*.class  ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/common/util/validator/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/interceptor
%__install -p -m644 WEB-INF/classes/jp/co/jprs/certmanager/web/interceptor/*.class ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/classes/jp/co/jprs/certmanager/web/interceptor/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/addAdmin
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/addOperator
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/deleteAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/reissueCertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/updateCertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/updateInformation
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/updatePassword
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/bootstrap
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/bootstrap/acceptAdmin
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/bootstrap/activateAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/bootstrap/issueOTU
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/internal
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/internal/internalDeleteAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/internal/internalReissueCertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/internal/registAdmin
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/internal/registMaintenance

%__install -p -m644 WEB-INF/mail/apply/addAdmin/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/addAdmin/
%__install -p -m644 WEB-INF/mail/apply/addOperator/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/addOperator/
%__install -p -m644 WEB-INF/mail/apply/deleteAdminAndOperator/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/deleteAdminAndOperator/
%__install -p -m644 WEB-INF/mail/apply/reissueCertificate/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/reissueCertificate/
%__install -p -m644 WEB-INF/mail/apply/updateCertificate/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/updateCertificate/
%__install -p -m644 WEB-INF/mail/apply/updateInformation/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/updateInformation/
%__install -p -m644 WEB-INF/mail/apply/updatePassword/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/apply/updatePassword/

%__install -p -m644 WEB-INF/mail/bootstrap/acceptAdmin/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/bootstrap/acceptAdmin/
%__install -p -m644 WEB-INF/mail/bootstrap/activateAdminAndOperator/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/bootstrap/activateAdminAndOperator/
%__install -p -m644 WEB-INF/mail/bootstrap/issueOTU/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/bootstrap/issueOTU/

%__install -p -m644 WEB-INF/mail/internal/internalDeleteAdminAndOperator/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/internal/internalDeleteAdminAndOperator/
%__install -p -m644 WEB-INF/mail/internal/internalReissueCertificate/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/internal/internalReissueCertificate/
%__install -p -m644 WEB-INF/mail/internal/registAdmin/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/internal/registAdmin/
%__install -p -m644 WEB-INF/mail/internal/registMaintenance/*.xml ${RPM_BUILD_ROOT}%{internal_dir}/WEB-INF/mail/internal/registMaintenance/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/common/css
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/common/img
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/common/js

%__install -p -m644 ui/common/css/*.css ${RPM_BUILD_ROOT}%{internal_dir}/ui/common/css/
%__install -p -m644 ui/common/img/*.gif ${RPM_BUILD_ROOT}%{internal_dir}/ui/common/img/
%__install -p -m644 ui/common/js/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/common/js/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-admin-theme/assets
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datepicker/css
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datepicker/js
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datepicker/locales
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datetimepicker/css
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datetimepicker/js
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datetimepicker/locales
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap/css
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap/img
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap/js
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/css
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/css
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/images
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/images/psd
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/js
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/swf
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/images
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/js
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/js

%__install -p -m644 ui/vendors/bootstrap-admin-theme/assets/*.css ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-admin-theme/assets/
%__install -p -m644 ui/vendors/bootstrap-admin-theme/assets/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-admin-theme/assets/

%__install -p -m644 ui/vendors/bootstrap-datepicker/css/*.css ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datepicker/css/
%__install -p -m644 ui/vendors/bootstrap-datepicker/js/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datepicker/js/
%__install -p -m644 ui/vendors/bootstrap-datepicker/locales/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datepicker/locales/

%__install -p -m644 ui/vendors/bootstrap-datetimepicker/css/*.css ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datetimepicker/css/
%__install -p -m644 ui/vendors/bootstrap-datetimepicker/js/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datetimepicker/js/
%__install -p -m644 ui/vendors/bootstrap-datetimepicker/locales/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap-datetimepicker/locales/

%__install -p -m644 ui/vendors/bootstrap/css/*.css ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap/css/
%__install -p -m644 ui/vendors/bootstrap/img/Thumbs.db ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap/img/
%__install -p -m644 ui/vendors/bootstrap/img/*.png ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap/img/
%__install -p -m644 ui/vendors/bootstrap/js/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/bootstrap/js/

%__install -p -m644 ui/vendors/datatables/css/*.css ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/css/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/css/*.css ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/css/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/images/*.png ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/images/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/images/psd/*.psd ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/images/psd/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/js/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/js/
%__install -p -m644 ui/vendors/datatables/extras/tabletools/swf/*.swf ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/extras/tabletools/swf/
%__install -p -m644 ui/vendors/datatables/images/*.png ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/images/
%__install -p -m644 ui/vendors/datatables/js/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/js/
%__install -p -m644 ui/vendors/datatables/js/*.txt ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/datatables/js/

%__install -p -m644 ui/vendors/js/*.js ${RPM_BUILD_ROOT}%{internal_dir}/ui/vendors/js/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/adminAndOperatorInformationOutput
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalDeleteAdminAndOperator
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalHome
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalIndex
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalInquiryInformation
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalReissueCertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/limitLicense
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/mailTemplateReference
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/manageCertificate
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/registAdmin
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/unregisteredAdminCancel
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/unregisteredAdminList
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/accountLockCancel
%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/registMaintenance

%__install -p -m644 ui/view/%{internal}/adminAndOperatorInformationOutput/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/adminAndOperatorInformationOutput/
%__install -p -m644 ui/view/%{internal}/internalDeleteAdminAndOperator/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalDeleteAdminAndOperator/
%__install -p -m644 ui/view/%{internal}/internalHome/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalHome/
%__install -p -m644 ui/view/%{internal}/internalIndex/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalIndex/
%__install -p -m644 ui/view/%{internal}/internalInquiryInformation/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalInquiryInformation/
%__install -p -m644 ui/view/%{internal}/internalReissueCertificate/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/internalReissueCertificate/
%__install -p -m644 ui/view/%{internal}/limitLicense/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/limitLicense/
%__install -p -m644 ui/view/%{internal}/mailTemplateReference/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/mailTemplateReference/
%__install -p -m644 ui/view/%{internal}/manageCertificate/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/manageCertificate/
%__install -p -m644 ui/view/%{internal}/registAdmin/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/registAdmin/
%__install -p -m644 ui/view/%{internal}/unregisteredAdminCancel/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/unregisteredAdminCancel/
%__install -p -m644 ui/view/%{internal}/unregisteredAdminList/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/unregisteredAdminList/
%__install -p -m644 ui/view/%{internal}/accountLockCancel/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/accountLockCancel/
%__install -p -m644 ui/view/%{internal}/registMaintenance/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/%{internal}/registMaintenance/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/common
%__install -p -m644 ui/view/common/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/common/

%__install -d ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/systemError
%__install -p -m644 ui/view/systemError/*.vm ${RPM_BUILD_ROOT}%{internal_dir}/ui/view/systemError/

popd

%clean
%__rm -rf ${RPM_BUILD_ROOT}/*

####################################
### cert-apply files section
####################################
%files -n %{name}-%{apply}
%defattr(-,%{account},%{account_group})
%dir %{webapps_dir}
%{apply_dir}
%dir %{base_dir}/htdocs

####################################
### cert-bootstrap files section
####################################
%files -n %{name}-%{bootstrap}
%defattr(-,%{account},%{account_group})
%dir %{webapps_dir}
%{bootstrap_dir}
%dir %{base_dir}/htdocs

####################################
### cert-internal files section
####################################
%files -n %{name}-%{internal}
%defattr(-,%{account},%{account_group})
%dir %{webapps_dir}
%{internal_dir}
%dir %{base_dir}/htdocs

### パッケージの更新履歴
%changelog
* Fri Jul 26 2019 m-kawashita <m-kawashita@jprs.co.jp>
- add: registMaintenance
* Thu Mar 07 2019 t-sakuma <t-sakuma@jprs.co.jp>
- first release
