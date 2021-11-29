# Conditional build
#

#
# rpmbuild -ba ~/rpm/SPECS/gjp-app-jpp.spec \
#              --define='version 20110804200913' \
#              --define='release PIW.019.REAL.REL'
#
%define account       dotjp0
%define account_group dotjp0
%define batch_account batch0
%define batch_group   batch0
%define world         real
%define job_world     agent-jpp
%define tld           gjp
%define internal_web  internal-web
%define servlet_world %{tld}-%{job_world}
%define servlet_internalweb_world %{tld}-%{internal_web}
%define fe1		f1
%define fe1basedir	/nfs/reg/data/%{fe1}/%{account}/
%define fe1appsdir	%{fe1basedir}/servlet/tomcat/webapps/
%define fe2		f2
%define fe2basedir	/nfs/reg/data/%{fe2}/%{account}/
%define fe2appsdir	%{fe2basedir}/servlet/tomcat/webapps/

%define jpp_package         agent-jpp
%define internalweb_package internal-web
%define noresident_package  noresident
%define queue_package       queue
%define scenario_package    scenario
%define config_package      config

%define servlet_world_pass  %{tld}-%{job_world}-pass
%define jpp_pass_package    agent-jpp-pass

%define standalone_dir     standalone
%define standalone_job_dir %{standalone_dir}/job
%define daemon_dir         daemon
%define daemon_job_dir     %{daemon_dir}/job
%define scenario_dir       scenario
%define scenario_job_dir   %{scenario_dir}/job
%define config_dir         config
%define batch_private_dir  /nfs/reg/share/private/backoffice/%{batch_account}

%define gjp_conf_tomcat        gjp-conf-tomcat-common
%define gjp_conf_tomcat_dir    gjp-conf-tomcat-dir
%define gjp_conf_tomcat_bin    gjp-conf-tomcat-bin
%define gjp_conf_tomcat_conf   gjp-conf-tomcat-conf
%define gjp_conf_tomcat_ver    20171101181223

# for JPP conf
%define gjp_conf_app           gjp-conf-agent-jpp
%define gjp_conf_app_ver       20171101181223

# for Internal-web conf
%define gjp_conf_app_internalweb     gjp-conf-agent-internal-web
%define gjp_conf_app_internalweb_ver 20171101181223

%define debug_package %{nil}
%define __jar_repack %{nil}

%bcond_with branch

Summary:	gjp Registry System
Summary(ja):	gjp registry System
Name:		gjp-app-jpp
Version:	%{version}
Release:	%{release}
License:	Copyright(c) 2010-2012 JPRS
Group:		Applications/Internet/Registry

%description
gjp Registry System

###
### gjp-app-jpp-common
###
%package -n %{name}-common
Summary:	gjp registry transaction system common
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-common >= %{gjp_conf_app_ver}
Requires:	%{gjp_conf_app_internalweb}-common >= %{gjp_conf_app_internalweb_ver}

%description -n %{name}-common
gjp registry transaction system common

###
### gjp-app-jpp-agent-jpp
###
%package -n %{name}-%{jpp_package}-%{fe1}
Summary:	gjp registry transaction system for agents for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe1} >= %{gjp_conf_app_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{jpp_package}-%{fe1}
gjp registry transaction system for agents for f1

%package -n %{name}-%{jpp_package}-%{fe2}
Summary:        gjp registry transaction system for agents for f2
Group:          Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe2} >= %{gjp_conf_app_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{jpp_package}-%{fe2}
gjp registry transaction system for agents for f2

###
### gjp-app-jpp-agent-jpp
###
%package -n %{name}-%{jpp_pass_package}-%{fe1}
Summary:	gjp registry transaction system for agents for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe1} >= %{gjp_conf_app_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{jpp_pass_package}-%{fe1}
gjp registry transaction system for agents for f1

%package -n %{name}-%{jpp_pass_package}-%{fe2}
Summary:        gjp registry transaction system for agents for f2
Group:          Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe2} >= %{gjp_conf_app_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{jpp_pass_package}-%{fe2}
gjp registry transaction system for agents for f2

###
### gjp-app-jpp-internal-web
###
%package -n %{name}-%{internalweb_package}-%{fe1}
Summary:	gjp registry internal-web system for agents for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app_internalweb}-%{fe1} >= %{gjp_conf_app_internalweb_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{internalweb_package}-%{fe1}
gjp registry internal-web system for agents for f1

%package -n %{name}-%{internalweb_package}-%{fe2}
Summary:        gjp registry internal-web system for agents for f2
Group:          Applications/Internet/Registry
Requires:	%{gjp_conf_app_internalweb}-%{fe2} >= %{gjp_conf_app_internalweb_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{internalweb_package}-%{fe2}
gjp registry internal-web system for agents for f2

###
### gjp-app-jpp-noresident
###
%package -n %{name}-%{noresident_package}-%{fe1}
Summary:	gjp registry(JPP) noresident system for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe1} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{noresident_package}-%{fe1}
gjp registry(JPP) noresident system for f1

%package -n %{name}-%{noresident_package}-%{fe2}
Summary:	gjp registry(JPP) noresident system for f2
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe2} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{noresident_package}-%{fe2}
gjp registry(JPP) noresident system for f2

###
### gjp-app-jpp-queue
###
%package -n %{name}-%{queue_package}-%{fe1}
Summary:	gjp registry(JPP) queue system for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe1} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{queue_package}-%{fe1}
gjp registry(JPP) queue system for f1

%package -n %{name}-%{queue_package}-%{fe2}
Summary:	gjp registry(JPP) queue system for f2
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe2} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{queue_package}-%{fe2}
gjp registry(JPP) queue system for f2

###
### gtld-app-jpp-scenario
###
%package -n %{name}-%{scenario_package}-%{fe1}
Summary:	gjp registry(JPP) scenario for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe1} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{scenario_package}-%{fe1}
gjp registry(JPP) scenario for f1

%package -n %{name}-%{scenario_package}-%{fe2}
Summary:	gjp registry(JPP) scenario for f2
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe2} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{scenario_package}-%{fe2}
gjp registry(JPP) scenario for f2

###
### gtld-app-jpp-config
###
%package -n %{name}-%{config_package}-%{fe1}
Summary:	gjp registry(JPP) config for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe1} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{config_package}-%{fe1}
gjp registry(JPP) config for f1

%package -n %{name}-%{config_package}-%{fe2}
Summary:	gjp registry(JPP) config for f2
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe2} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{config_package}-%{fe2}
gjp registry(JPP) config for f2

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
cd ./src/domain/registry
/usr/local/ant/bin/ant -f build.release.xml \
    -Dusername=%{account}/%{job_world} \
    -Daplname=%{servlet_world} \
    -Dbatchusername=%{batch_account} \
    -Dworldname=%{world}

%install
[ "${RPM_BUILD_ROOT}" != "/" ] && %__rm -rf ${RPM_BUILD_ROOT}

export JAR_BIN=/usr/local/jdk1.8/bin/jar

pushd ./src/domain/registry/release
%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/%{servlet_world}
%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/%{servlet_internalweb_world}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/%{servlet_world}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/%{servlet_internalweb_world}
%__install -p -m644 %{servlet_world}.war             ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 %{servlet_internalweb_world}.war ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 %{servlet_world}.war             ${RPM_BUILD_ROOT}/%{fe2appsdir}
%__install -p -m644 %{servlet_internalweb_world}.war ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/%{servlet_world_pass}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/%{servlet_world_pass}
%__install -p -m644 %{servlet_world_pass}.war      ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 %{servlet_world_pass}.war      ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/%{standalone_job_dir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/%{standalone_job_dir}
%__install -p -m644 %{tld}-%{noresident_package}.zip   ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}
%__install -p -m644 %{tld}-%{noresident_package}.zip   ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/%{daemon_job_dir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/%{daemon_job_dir}
%__install -p -m644 %{tld}-%{queue_package}.zip        ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}
%__install -p -m644 %{tld}-%{queue_package}.zip        ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/%{scenario_job_dir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/%{scenario_job_dir}
%__install -p -m644 %{scenario_package}.zip     ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}
%__install -p -m644 %{scenario_package}.zip     ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/%{config_dir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/%{config_dir}
%__install -p -m644 %{config_package}.zip     ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}
%__install -p -m644 %{config_package}.zip     ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}
popd

%__mkdir_p ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/htdocs/%{internal_web}
%__mkdir_p ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/htdocs/%{internal_web}

%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/archive
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/archive/trc-mail
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/snapshot
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/snapshot/drp
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/print
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/pref-spool-apply
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/pref-spool-apply/tmp
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/bill
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/rev-dom-history
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/ns
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/ns-set
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/dom-trans
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/dom-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/dom
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/host
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/redirect
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/pub
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/agent
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/reg-trans
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/reg-trans-apply
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/signingkey
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/recover-daily
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/recover-monthly
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/reg
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/lists/expire
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/office
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/office/acc
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/office/acc/mlt-st
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/office/acc/fromPC
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/office/acc/toPC
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/acc
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/acc/forms
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/acc/forms/daily
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/acc/forms/monthly
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/acc/forms/quater
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/htdocs
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/htdocs/list
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/htdocs/list/redirect
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/fb
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/fb/from-bank
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/fb/backup
%__install -d ${RPM_BUILD_ROOT}%{batch_private_dir}/fb/to-bank

%pre -n %{name}-%{jpp_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_world}/*

%pre -n %{name}-%{jpp_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_world}/*

%pre -n %{name}-%{jpp_pass_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_world_pass}/*

%pre -n %{name}-%{jpp_pass_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_world_pass}/*

%pre -n %{name}-%{internalweb_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internalweb_world}/*

%pre -n %{name}-%{internalweb_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internalweb_world}/*

%pre -n %{name}-%{noresident_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}/%{standalone_job_dir}/*

%pre -n %{name}-%{noresident_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}/%{standalone_job_dir}/*

%pre -n %{name}-%{queue_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}/%{daemon_job_dir}/*

%pre -n %{name}-%{queue_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}/%{daemon_job_dir}/*

%pre -n %{name}-%{scenario_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}/%{scenario_job_dir}/*

%pre -n %{name}-%{scenario_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}/%{scenario_job_dir}/*

%preun -n %{name}-%{jpp_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_world}/*
fi

%preun -n %{name}-%{jpp_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_world}/*
fi

%preun -n %{name}-%{jpp_pass_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_world_pass}/*
fi

%preun -n %{name}-%{jpp_pass_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_world_pass}/*
fi

%preun -n %{name}-%{internalweb_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_internalweb_world}/*
fi

%preun -n %{name}-%{internalweb_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_internalweb_world}/*
fi

%preun -n %{name}-%{noresident_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}/%{standalone_job_dir}/*
fi

%preun -n %{name}-%{noresident_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}/%{standalone_job_dir}/*
fi

%preun -n %{name}-%{queue_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}/%{daemon_job_dir}/*
fi

%preun -n %{name}-%{queue_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}/%{daemon_job_dir}/*
fi

%preun -n %{name}-%{scenario_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}/%{scenario_job_dir}/*
fi

%preun -n %{name}-%{scenario_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}/%{scenario_job_dir}/*
fi

%preun -n %{name}-%{config_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}/%{config_dir}/*
fi

%preun -n %{name}-%{config_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}/%{config_dir}/*
fi

%post -n %{name}-%{jpp_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./%{servlet_world}.war -d ./%{servlet_world}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_world}
popd

%post -n %{name}-%{jpp_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./%{servlet_world}.war -d ./%{servlet_world}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_world}
popd

%post -n %{name}-%{jpp_pass_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./%{servlet_world_pass}.war -d ./%{servlet_world_pass}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_world_pass}
popd

%post -n %{name}-%{jpp_pass_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./%{servlet_world_pass}.war -d ./%{servlet_world_pass}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_world_pass}
popd

%post -n %{name}-%{internalweb_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./%{servlet_internalweb_world}.war -d ./%{servlet_internalweb_world}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_internalweb_world}
popd

%post -n %{name}-%{internalweb_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./%{servlet_internalweb_world}.war -d ./%{servlet_internalweb_world}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_internalweb_world}
popd

%post -n %{name}-%{noresident_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}
%__unzip ./%{tld}-%{noresident_package}.zip -d ./%{standalone_job_dir}
%__chown -Rhf %{account}:%{account_group} ./%{standalone_job_dir}
popd

%post -n %{name}-%{noresident_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}
%__unzip ./%{tld}-%{noresident_package}.zip -d ./%{standalone_job_dir}
%__chown -Rhf %{account}:%{account_group} ./%{standalone_job_dir}
popd

%post -n %{name}-%{queue_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}
%__unzip ./%{tld}-%{queue_package}.zip -d ./%{daemon_job_dir}
%__chown -Rhf %{account}:%{account_group} ./%{daemon_job_dir}
popd

%post -n %{name}-%{queue_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}
%__unzip ./%{tld}-%{queue_package}.zip -d ./%{daemon_job_dir}
%__chown -Rhf %{account}:%{account_group} ./%{daemon_job_dir}
popd

%post -n %{name}-%{scenario_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}
%__unzip ./%{scenario_package}.zip -d ./%{scenario_job_dir}
%__chmod 0755 ./%{scenario_job_dir}/*.sh
%__chmod 0755 ./%{scenario_job_dir}/dr/bin/*.sh
%__chown -Rhf %{account}:%{account_group} ./%{scenario_job_dir}
popd

%post -n %{name}-%{scenario_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}
%__unzip ./%{scenario_package}.zip -d ./%{scenario_job_dir}
%__chmod 0755 ./%{scenario_job_dir}/*.sh
%__chmod 0755 ./%{scenario_job_dir}/dr/bin/*.sh
%__chown -Rhf %{account}:%{account_group} ./%{scenario_job_dir}
popd

%post -n %{name}-%{config_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}
unzip -o ./%{config_package}.zip -d ./%{config_dir}
%__chown -Rhf %{account}:%{account_group} ./%{config_dir}
popd

%post -n %{name}-%{config_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}
unzip -o ./%{config_package}.zip -d ./%{config_dir}
%__chown -Rhf %{account}:%{account_group} ./%{config_dir}
popd

%clean
%__rm -rf ${RPM_BUILD_ROOT}

%files -n %{name}-common
%defattr(755,%{batch_account},%{batch_group},755)
%dir %{batch_private_dir}/lists
%dir %{batch_private_dir}/acc
%dir %{batch_private_dir}/acc/forms
%dir %{batch_private_dir}/office
%dir %{batch_private_dir}/office/acc
%dir %{batch_private_dir}/snapshot
%dir %{batch_private_dir}/htdocs
%dir %{batch_private_dir}/fb
%defattr(2775,%{batch_account},%{batch_group},2775)
%dir %{batch_private_dir}/archive
%dir %{batch_private_dir}/archive/trc-mail
%dir %{batch_private_dir}/snapshot/drp
%dir %{batch_private_dir}/lists/pref-spool-apply
%dir %{batch_private_dir}/lists/pref-spool-apply/tmp
%dir %{batch_private_dir}/lists/bill
%dir %{batch_private_dir}/lists/rev-dom-history
%dir %{batch_private_dir}/lists/ns
%dir %{batch_private_dir}/lists/ns-set
%dir %{batch_private_dir}/lists/dom-trans
%dir %{batch_private_dir}/lists/dom-trans-apply
%dir %{batch_private_dir}/lists/dom
%dir %{batch_private_dir}/lists/host
%dir %{batch_private_dir}/lists/redirect
%dir %{batch_private_dir}/lists/pub
%dir %{batch_private_dir}/lists/agent
%dir %{batch_private_dir}/lists/reg-trans
%dir %{batch_private_dir}/lists/reg-trans-apply
%dir %{batch_private_dir}/lists/signingkey
%dir %{batch_private_dir}/lists/recover-daily
%dir %{batch_private_dir}/lists/recover-monthly
%dir %{batch_private_dir}/lists/reg
%dir %{batch_private_dir}/lists/expire
%dir %{batch_private_dir}/acc/forms/daily
%dir %{batch_private_dir}/acc/forms/monthly
%dir %{batch_private_dir}/acc/forms/quater
%dir %{batch_private_dir}/office/acc/toPC
%dir %{batch_private_dir}/htdocs/list
%dir %{batch_private_dir}/htdocs/list/redirect
%dir %{batch_private_dir}/fb/from-bank
%dir %{batch_private_dir}/fb/backup
%dir %{batch_private_dir}/fb/to-bank
%dir %{batch_private_dir}/office/acc/fromPC
%defattr(775,%{batch_account},%{batch_group},775)
%dir %{batch_private_dir}/print
%dir %{batch_private_dir}/office/acc/mlt-st

%files -n %{name}-%{jpp_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1appsdir}/%{servlet_world}
%{fe1appsdir}/%{servlet_world}.war

%files -n %{name}-%{jpp_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2appsdir}/%{servlet_world}
%{fe2appsdir}/%{servlet_world}.war

%files -n %{name}-%{jpp_pass_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1appsdir}/%{servlet_world_pass}
%{fe1appsdir}/%{servlet_world_pass}.war

%files -n %{name}-%{jpp_pass_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2appsdir}/%{servlet_world_pass}
%{fe2appsdir}/%{servlet_world_pass}.war

%files -n %{name}-%{internalweb_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1appsdir}/%{servlet_internalweb_world}
%dir %{fe1basedir}/%{job_world}/htdocs
%dir %{fe1basedir}/%{job_world}/htdocs/%{internal_web}
%{fe1appsdir}/%{servlet_internalweb_world}.war

%files -n %{name}-%{internalweb_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2appsdir}/%{servlet_internalweb_world}
%dir %{fe2basedir}/%{job_world}/htdocs
%dir %{fe2basedir}/%{job_world}/htdocs/%{internal_web}
%{fe2appsdir}/%{servlet_internalweb_world}.war


%files -n %{name}-%{noresident_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1basedir}/%{job_world}/%{standalone_dir}
%dir %{fe1basedir}/%{job_world}/%{standalone_job_dir}
%{fe1basedir}/%{job_world}/%{tld}-%{noresident_package}.zip

%files -n %{name}-%{noresident_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2basedir}/%{job_world}/%{standalone_dir}
%dir %{fe2basedir}/%{job_world}/%{standalone_job_dir}
%{fe2basedir}/%{job_world}/%{tld}-%{noresident_package}.zip


%files -n %{name}-%{queue_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1basedir}/%{job_world}/%{daemon_dir}
%dir %{fe1basedir}/%{job_world}/%{daemon_job_dir}
%{fe1basedir}/%{job_world}/%{tld}-%{queue_package}.zip

%files -n %{name}-%{queue_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2basedir}/%{job_world}/%{daemon_dir}
%dir %{fe2basedir}/%{job_world}/%{daemon_job_dir}
%{fe2basedir}/%{job_world}/%{tld}-%{queue_package}.zip


%files -n %{name}-%{scenario_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1basedir}/%{job_world}/%{scenario_dir}
%dir %{fe1basedir}/%{job_world}/%{scenario_job_dir}
%{fe1basedir}/%{job_world}/%{scenario_package}.zip

%files -n %{name}-%{scenario_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2basedir}/%{job_world}/%{scenario_dir}
%dir %{fe2basedir}/%{job_world}/%{scenario_job_dir}
%{fe2basedir}/%{job_world}/%{scenario_package}.zip


%files -n %{name}-%{config_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1basedir}/%{job_world}/%{config_dir}
%{fe1basedir}/%{job_world}/%{config_package}.zip

%files -n %{name}-%{config_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2basedir}/%{job_world}/%{config_dir}
%{fe2basedir}/%{job_world}/%{config_package}.zip

%changelog
* Tue Mar 20 2018 Sumie Satou <su-sato@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20180320173948
- update: gjp-conf-agent-jpp           20180320173948
- update: gjp_conf_app_internalweb_ver 20180320173948

* Mon Mar 19 2018 Sumie Satou <su-sato@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20180319175658
- update: gjp-conf-agent-jpp           20180319175658
- update: gjp_conf_app_internalweb_ver 20180319175658

* Wed Nov 1 2017 Sumie Satou <su-sato@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20171101181223
- update: gjp-conf-agent-jpp           20171101181223
- update: gjp_conf_app_internalweb_ver 20171101181223

* Wed Mar 9 2016 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20160208180313

* Thu Dec 17 2015  Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20151216172505

* Thu Nov 26 2015  Shigeru Hamamoto  <s-hamamoto@jprs.co.jp>
- update: JAVA_HOME /usr/local/jdk1.8/ 
- update: JAR_BIN   /usr/local/jdk1.8/bin/jar

* Tue Oct 28 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_app_ver             20141028113328
- update: gjp_conf_app_internalweb_ver 20141028113328

* Fri Sep 5 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- add: gjp-app-jpp-agent-jpp-pass

* Thu Mar 13 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20140313120739

* Fri Mar 7 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20140306215800
- update: gjp_conf_app_ver             20140306215800
- update: gjp_conf_app_internalweb_ver 20140306215800

* Tue Feb 25 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: chmod 0755 %{scenario_job_dir}/dr/bin/*.sh

* Fri Jan 18 2013 Tomohiro Nakagawa <t-nakagw@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20130111184753
- update: gjp_conf_app_ver             20130111184753
- update: gjp_conf_app_internalweb_ver 20130111184753

* Thu Dec 27 2012 Tomohiro Nakagawa <t-nakagw@jprs.co.jp>
- chmod 2775 %{batch_private_dir}/office/acc/fromPC 

* Thu Dec 13 2012  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gjp_conf_app_ver       20121212194938
- update: gjp_conf_app_internalweb_ver 20121212194938

* Fri Nov 9 2012  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gjp_conf_tomcat_ver  20121109130634
- update: JAVA_HOME /usr/local/jdk1.6.0_37/ 
- update: JAR_BIN   /usr/local/jdk1.6.0_37/bin/jar

* Tue Feb 21 2012 k-kosuga <k-kosuga@jprs.co.jp>
- first release
