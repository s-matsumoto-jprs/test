# Conditional build
#

#
# rpmbuild -ba ~/rpm/SPECS/cert-batch.spec \
#              --define='version 20170919203743' \
#              --define='release PIW.019.REAL.REL'
#

%define account        app000
%define account_group  app000
%define world          real
%define base_dir       /data/app001
%define bin_dir        %{base_dir}/bin
%define conf_dir       %{base_dir}/conf
%define lib_dir        %{base_dir}/lib
%define mail_dir       %{base_dir}/mail_template

%define buld_package   job

%define debug_package %{nil}
%define __jar_repack %{nil}

%bcond_with branch
%bcond_with real

%if %{with real}
%define environment real
%else
%define environment jail
%endif

### パッケージ基本情報
Summary:     Certificate Management System
Summary(ja): 証明書管理I/F
Name:        cert-app-batch
Version:     %{version}
Release:     %{release}.%{environment}
License:     Copyright(c) JPRS
Group:       Applications/Other/Cert

%description
Certificate Management System

###
### cert-batch
###
%package -n %{name}-%{buld_package}
Summary:  Certificate Management System
Group:    Applications/Other/Cert

%description -n %{name}-%{buld_package}
Certificate Management System

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
  -f build_batch.xml \
  -Dtarget_world=${TNAME} \
  make-package

%install
[ "${RPM_BUILD_ROOT}" != "/" ] && %__rm -rf ${RPM_BUILD_ROOT}

export JAR_BIN=/usr/lib/jvm/java-1.8.0-openjdk/bin/jar

pushd ./src/cert/agent/buildroot/batchroot
%__install -d ${RPM_BUILD_ROOT}%{bin_dir}
%__install -p -m755 bin/*.sh ${RPM_BUILD_ROOT}%{bin_dir}/

%__install -d ${RPM_BUILD_ROOT}%{conf_dir}
%__install -p -m644 conf/.env ${RPM_BUILD_ROOT}%{conf_dir}/
%__install -p -m644 conf/*.dicon ${RPM_BUILD_ROOT}%{conf_dir}/
%__install -p -m644 conf/*.xml ${RPM_BUILD_ROOT}%{conf_dir}/
%__install -p -m644 conf/*.csv ${RPM_BUILD_ROOT}%{conf_dir}/

%__install -d ${RPM_BUILD_ROOT}%{lib_dir}
%__install -p -m644 lib/*.jar ${RPM_BUILD_ROOT}%{lib_dir}/

%__install -d ${RPM_BUILD_ROOT}%{mail_dir}/advanceNotificationCertificateTermination
%__install -d ${RPM_BUILD_ROOT}%{mail_dir}/confirmationTotalLisence
%__install -d ${RPM_BUILD_ROOT}%{mail_dir}/confirmationTotalLisenceEachAgent
%__install -d ${RPM_BUILD_ROOT}%{mail_dir}/deleteLostCertificateAccount
%__install -d ${RPM_BUILD_ROOT}%{mail_dir}/deletePendingActivateAccount
%__install -d ${RPM_BUILD_ROOT}%{mail_dir}/deletePendingRegistAccount
%__install -d ${RPM_BUILD_ROOT}%{mail_dir}/deletePublicationOTUAccount
%__install -d ${RPM_BUILD_ROOT}%{mail_dir}/deleteUseStopTargetAccount
%__install -d ${RPM_BUILD_ROOT}%{mail_dir}/noticeUseStopTargetAccount

%__install -p -m644 mail_template/advanceNotificationCertificateTermination/*.xml ${RPM_BUILD_ROOT}%{mail_dir}/advanceNotificationCertificateTermination/
%__install -p -m644 mail_template/confirmationTotalLisence/*.xml ${RPM_BUILD_ROOT}%{mail_dir}/confirmationTotalLisence/
%__install -p -m644 mail_template/confirmationTotalLisenceEachAgent/*.xml ${RPM_BUILD_ROOT}%{mail_dir}/confirmationTotalLisenceEachAgent/
%__install -p -m644 mail_template/deleteLostCertificateAccount/*.xml ${RPM_BUILD_ROOT}%{mail_dir}/deleteLostCertificateAccount/
%__install -p -m644 mail_template/deletePendingActivateAccount/*.xml ${RPM_BUILD_ROOT}%{mail_dir}/deletePendingActivateAccount/
%__install -p -m644 mail_template/deletePendingRegistAccount/*.xml ${RPM_BUILD_ROOT}%{mail_dir}/deletePendingRegistAccount/
%__install -p -m644 mail_template/deletePublicationOTUAccount/*.xml ${RPM_BUILD_ROOT}%{mail_dir}/deletePublicationOTUAccount/
%__install -p -m644 mail_template/deleteUseStopTargetAccount/*.xml ${RPM_BUILD_ROOT}%{mail_dir}/deleteUseStopTargetAccount/
%__install -p -m644 mail_template/noticeUseStopTargetAccount/*.xml ${RPM_BUILD_ROOT}%{mail_dir}/noticeUseStopTargetAccount/

popd

%clean
%__rm -rf ${RPM_BUILD_ROOT}%

%files -n %{name}-%{buld_package}
%defattr(-,%{account},%{account_group})
%{bin_dir}
%{conf_dir}
%{lib_dir}
%{mail_dir}


### パッケージの更新履歴
%changelog
* Mon Feb 04 2019 m-kawashita <m-kawashita@jprs.co.jp>
- first release
