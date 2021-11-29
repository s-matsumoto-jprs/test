# Conditional build
#

#
# rpmbuild -ba ~/rpm/SPECS/gjp-tb-app-web.spec \
#              --define='version 20110804200913' \
#              --define='release PIW.019.REAL.REL'
#
%define account        dotjp0
%define account_group  dotjp0
%define batch0_account dotjp0
%define batch0_group   dotjp0
%define tb_file_account      tbbatch0
%define world         demo
%define job_world     tb-agent-web
%define tld           gjp
%define servlet_world %{tld}-%{job_world}
%define fe1		f1
%define fe1basedir	/nfs/reg/data/%{fe1}/%{account}/
%define fe1appsdir	%{fe1basedir}/servlet/tomcat/webapps/
%define fe2		f2
%define fe2basedir	/nfs/reg/data/%{fe2}/%{account}/
%define fe2appsdir	%{fe2basedir}/servlet/tomcat/webapps/

%define web_package        agent-web
%define scenario_package   scenario

%define scenario_dir       scenario
%define scenario_job_dir   %{scenario_dir}/job
%define batch0_public_dir  /nfs/reg/share/public/download/%{tb_file_account}

%define web_package_pass     agent-web-pass
%define job_world_pass       tb-agent-web-pass
%define servlet_world_pass   %{tld}-%{job_world_pass}

%define agency               agency
%define agency_world         %{tld}-tb-%{agency}

%define gjp_conf_tomcat        gjp-conf-tomcat-common
%define gjp_conf_tomcat_dir    gjp-conf-tomcat-dir
%define gjp_conf_tomcat_bin    gjp-conf-tomcat-bin
%define gjp_conf_tomcat_conf   gjp-conf-tomcat-conf
%define gjp_conf_tomcat_ver    20171101181223

%define gjp_conf_app           gjp-conf-tb-agent-web
%define gjp_conf_app_ver       20171101181223

%define debug_package %{nil}
%define __jar_repack %{nil}

%bcond_with branch

Summary:	gjp Registry System 
Summary(ja):	gjp Registry System 
Name:		gjp-tb-app-web
Version:	%{version}
Release:	%{release}
License:	Copyright(c) 2010-2012 JPRS
Group:		Applications/Internet/Registry

%description
gjp Registry System

###
### gjp-tb-app-web-common
###
%package -n %{name}-common
Summary:	 gjp registry agent-web system common
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-common >= %{gjp_conf_app_ver}

%description -n %{name}-common
gjp registry agent-web system common

###
### gjp-tb-app-web-agent-web
###
%package -n %{name}-%{web_package}-%{fe1}
Summary:	gjp registry agent-web system for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe1} >= %{gjp_conf_app_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{web_package}-%{fe1}
gjp registry agent-web system for f1

%package -n %{name}-%{web_package}-%{fe2}
Summary:        gjp registry agent-web system for f2
Group:          Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe2} >= %{gjp_conf_app_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{web_package}-%{fe2}
gjp registry agent-web system for f2

###
### gjp-tb-app-web-scenario
###
%package -n %{name}-%{scenario_package}-%{fe1}
Summary:	gjp registry scenario for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe1} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{scenario_package}-%{fe1}
gjp registry scenario for f1

%package -n %{name}-%{scenario_package}-%{fe2}
Summary:	gjp registry scenario for f2
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe2} >= %{gjp_conf_app_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{scenario_package}-%{fe2}
PASTA - registrar scenario for f2


###
### gjp-tb-app-web-agent-web-pass
###
%package -n %{name}-%{web_package_pass}-%{fe1}
Summary:	gjp registry agent-web system for f1
Group:		Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe1} >= %{gjp_conf_app_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe1} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{web_package_pass}-%{fe1}
gjp registry agent-web system for f1

%package -n %{name}-%{web_package_pass}-%{fe2}
Summary:        gjp registry agent-web system for f2
Group:          Applications/Internet/Registry
Requires:	%{gjp_conf_app}-%{fe2} >= %{gjp_conf_app_ver}
Requires:	%{gjp_conf_tomcat} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_dir}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_bin}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{gjp_conf_tomcat_conf}-%{fe2} >= %{gjp_conf_tomcat_ver}
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{name}-%{web_package_pass}-%{fe2}
gjp registry agent-web system for f2

###
### gjp-tb-app-web-agency
###
%package -n %{name}-%{agency}-%{fe1}
Summary:        gjp registry agent-web system for f1
Group:          Applications/Internet/Registry

%description -n %{name}-%{agency}-%{fe1}
gjp registry agent-web system for f1

%package -n %{name}-%{agency}-%{fe2}
Summary:        gjp registry agent-web system for f2
Group:          Applications/Internet/Registry

%description -n %{name}-%{agency}-%{fe2}
gjp registry agent-web system for f2

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
/usr/local/ant/bin/ant \
   -f build.gjp.release.xml \
   -Drelease.mode=%{world}

%install
[ "${RPM_BUILD_ROOT}" != "/" ] && %__rm -rf ${RPM_BUILD_ROOT}

export JAR_BIN=/usr/local/jdk1.8/bin/jar

pushd ./src/domain/registrar/release
%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/%{servlet_world}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/%{servlet_world}
%__install -p -m644 %{servlet_world}.war      ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 %{servlet_world}.war      ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/%{scenario_job_dir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/%{scenario_job_dir}
%__install -p -m644 %{scenario_package}.zip     ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}
%__install -p -m644 %{scenario_package}.zip     ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/%{servlet_world_pass}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/%{servlet_world_pass}
%__install -p -m644 %{servlet_world_pass}.war      ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 %{servlet_world_pass}.war      ${RPM_BUILD_ROOT}/%{fe2appsdir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world_pass}/%{scenario_job_dir}
%__install -d ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world_pass}/%{scenario_job_dir}

%__install -d ${RPM_BUILD_ROOT}/%{fe1appsdir}/%{agency_world}
%__install -d ${RPM_BUILD_ROOT}/%{fe2appsdir}/%{agency_world}
%__install -p -m644 %{agency_world}.war      ${RPM_BUILD_ROOT}/%{fe1appsdir}
%__install -p -m644 %{agency_world}.war      ${RPM_BUILD_ROOT}/%{fe2appsdir}
popd

pushd ./src/domain/registrar/config/%{tld}-%{world}/agent-web
%__mkdir_p ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/config
%__mkdir_p ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/config
%__cp -pr ./ ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/config/agent-web
%__cp -pr ./ ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/config/agent-web
popd

pushd ./src/domain/registrar/config/%{tld}-%{world}/agent-web-pass
%__mkdir_p ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world_pass}/config
%__mkdir_p ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world_pass}/config
%__cp -pr ./ ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world_pass}/config/agent-web
%__cp -pr ./ ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world_pass}/config/agent-web
popd

%__mkdir_p ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/htdocs
%__ln_s /data/dotjp0/servlet/tomcat/webapps/%{servlet_world}/img \
        ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world}/htdocs/img
%__mkdir_p ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/htdocs
%__ln_s /data/dotjp0/servlet/tomcat/webapps/%{servlet_world}/img \
        ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world}/htdocs/img

%__mkdir_p ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world_pass}/htdocs
%__ln_s /data/dotjp0/servlet/tomcat/webapps/%{servlet_world_pass}/img \
        ${RPM_BUILD_ROOT}/%{fe1basedir}/%{job_world_pass}/htdocs/img
%__mkdir_p ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world_pass}/htdocs
%__ln_s /data/dotjp0/servlet/tomcat/webapps/%{servlet_world_pass}/img \
        ${RPM_BUILD_ROOT}/%{fe2basedir}/%{job_world_pass}/htdocs/img


#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/agent
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/bad-ns
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/bill
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/dns-err-del
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/dnsqc
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/dom
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/dom-trans
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/dom-trans-apply
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/expire
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/host
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/ns
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/ns-set
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/pub
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/recover-daily
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/recover-monthly
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/redirect
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/reg
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/reg-trans
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/reg-trans-apply
#%__install -d ${RPM_BUILD_ROOT}%{batch0_public_dir}/lists/signingkey

%pre -n %{name}-%{web_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_world}/*

%pre -n %{name}-%{web_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_world}/*

%pre -n %{name}-%{web_package_pass}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_world_pass}/*

%pre -n %{name}-%{web_package_pass}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_world_pass}/*

%pre -n %{name}-%{scenario_package}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}/%{scenario_job_dir}/*

%pre -n %{name}-%{scenario_package}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}/%{scenario_job_dir}/*

%pre -n %{name}-%{agency}-%{fe1}
%__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{agency_world}/*

%pre -n %{name}-%{agency}-%{fe2}
%__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{agency_world}/*

%preun -n %{name}-%{web_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_world}/*
fi

%preun -n %{name}-%{web_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_world}/*
fi

%preun -n %{name}-%{web_package_pass}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{servlet_world_pass}/*
fi

%preun -n %{name}-%{web_package_pass}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{servlet_world_pass}/*
fi

%preun -n %{name}-%{scenario_package}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}/%{scenario_job_dir}/*
fi

%preun -n %{name}-%{scenario_package}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}/%{scenario_job_dir}/*
fi

%preun -n %{name}-%{agency}-%{fe1}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe1appsdir}/%{agency_world}/*
fi

%preun -n %{name}-%{agency}-%{fe2}
if [ "$1" = 0 ]; then
    %__rm -rf ${RPM_BUILD_ROOT}%{fe2appsdir}/%{agency_world}/*
fi

%post -n %{name}-%{web_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./%{servlet_world}.war -d ./%{servlet_world}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_world}
popd

%post -n %{name}-%{web_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./%{servlet_world}.war -d ./%{servlet_world}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_world}
popd

%post -n %{name}-%{web_package_pass}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./%{servlet_world_pass}.war -d ./%{servlet_world_pass}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_world_pass}
popd

%post -n %{name}-%{web_package_pass}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./%{servlet_world_pass}.war -d ./%{servlet_world_pass}
%__chown -Rhf %{account}:%{account_group} ./%{servlet_world_pass}
popd

%post -n %{name}-%{scenario_package}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1basedir}/%{job_world}
%__unzip ./%{scenario_package}.zip -d ./%{scenario_job_dir}
%__chmod 0755 ./%{scenario_job_dir}/*.sh
%__chown -Rhf %{account}:%{account_group} ./%{scenario_job_dir}
popd

%post -n %{name}-%{scenario_package}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2basedir}/%{job_world}
%__unzip ./%{scenario_package}.zip -d ./%{scenario_job_dir}
%__chmod 0755 ./%{scenario_job_dir}/*.sh
%__chown -Rhf %{account}:%{account_group} ./%{scenario_job_dir}
popd

%post -n %{name}-%{agency}-%{fe1}
pushd ${RPM_BUILD_ROOT}%{fe1appsdir}
%__unzip ./%{agency_world}.war -d ./%{agency_world}
%__chown -Rhf %{account}:%{account_group} ./%{agency_world}
popd

%post -n %{name}-%{agency}-%{fe2}
pushd ${RPM_BUILD_ROOT}%{fe2appsdir}
%__unzip ./%{agency_world}.war -d ./%{agency_world}
%__chown -Rhf %{account}:%{account_group} ./%{agency_world}
popd

%clean
%__rm -rf ${RPM_BUILD_ROOT}

%files -n %{name}-common
%defattr(757,%{batch0_account},%{batch0_group},757)
#%dir %{batch0_public_dir}/lists
#%dir %{batch0_public_dir}/lists/bad-ns
#%dir %{batch0_public_dir}/lists/bill
#%dir %{batch0_public_dir}/lists/dns-err-del
#%dir %{batch0_public_dir}/lists/dnsqc
#%dir %{batch0_public_dir}/lists/expire
#%dir %{batch0_public_dir}/lists/recover-monthly
%defattr(2777,%{batch0_account},%{batch0_group},2777)
#%dir %{batch0_public_dir}/lists/ns
#%dir %{batch0_public_dir}/lists/ns-set
#%dir %{batch0_public_dir}/lists/dom-trans
#%dir %{batch0_public_dir}/lists/dom-trans-apply
#%dir %{batch0_public_dir}/lists/dom
#%dir %{batch0_public_dir}/lists/host
#%dir %{batch0_public_dir}/lists/redirect
#%dir %{batch0_public_dir}/lists/pub
#%dir %{batch0_public_dir}/lists/agent
#%dir %{batch0_public_dir}/lists/reg-trans
#%dir %{batch0_public_dir}/lists/reg-trans-apply
#%dir %{batch0_public_dir}/lists/signingkey
#%dir %{batch0_public_dir}/lists/recover-daily
#%dir %{batch0_public_dir}/lists/reg

%files -n %{name}-%{web_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1appsdir}/%{servlet_world}
%dir %{fe1basedir}/%{job_world}
%dir %{fe1basedir}/%{job_world}/config
%dir %{fe1basedir}/%{job_world}/config/agent-web
%dir %{fe1basedir}/%{job_world}/htdocs
%{fe1appsdir}/%{servlet_world}.war
%{fe1basedir}/%{job_world}/config/agent-web/gjp_transaction.xml
%{fe1basedir}/%{job_world}/config/agent-web/log4j.xml
%{fe1basedir}/%{job_world}/htdocs/img

%files -n %{name}-%{web_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2appsdir}/%{servlet_world}
%dir %{fe2basedir}/%{job_world}
%dir %{fe2basedir}/%{job_world}/config
%dir %{fe2basedir}/%{job_world}/config/agent-web
%dir %{fe2basedir}/%{job_world}/htdocs
%{fe2appsdir}/%{servlet_world}.war
%{fe2basedir}/%{job_world}/config/agent-web/gjp_transaction.xml
%{fe2basedir}/%{job_world}/config/agent-web/log4j.xml
%{fe2basedir}/%{job_world}/htdocs/img

%files -n %{name}-%{web_package_pass}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1appsdir}/%{servlet_world_pass}
%dir %{fe1basedir}/%{job_world_pass}
%dir %{fe1basedir}/%{job_world_pass}/config
%dir %{fe1basedir}/%{job_world_pass}/config/agent-web
%dir %{fe1basedir}/%{job_world_pass}/htdocs
%{fe1appsdir}/%{servlet_world_pass}.war
%{fe1basedir}/%{job_world_pass}/config/agent-web/gjp_transaction.xml
%{fe1basedir}/%{job_world_pass}/config/agent-web/log4j.xml
%{fe1basedir}/%{job_world_pass}/htdocs/img

%files -n %{name}-%{web_package_pass}-%{fe2}
%defattr(-,%{account},%{account_group},-)
%dir %{fe2appsdir}/%{servlet_world_pass}
%dir %{fe2basedir}/%{job_world_pass}
%dir %{fe2basedir}/%{job_world_pass}/config
%dir %{fe2basedir}/%{job_world_pass}/config/agent-web
%dir %{fe2basedir}/%{job_world_pass}/htdocs
%{fe2appsdir}/%{servlet_world_pass}.war
%{fe2basedir}/%{job_world_pass}/config/agent-web/gjp_transaction.xml
%{fe2basedir}/%{job_world_pass}/config/agent-web/log4j.xml
%{fe2basedir}/%{job_world_pass}/htdocs/img

%files -n %{name}-%{scenario_package}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1basedir}/%{job_world}/%{scenario_dir}
%dir %{fe1basedir}/%{job_world}/%{scenario_job_dir}
%{fe1basedir}/%{job_world}/%{scenario_package}.zip
%dir %{fe1basedir}/%{job_world_pass}/%{scenario_dir}
%dir %{fe1basedir}/%{job_world_pass}/%{scenario_job_dir}

%files -n %{name}-%{scenario_package}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2basedir}/%{job_world}/%{scenario_dir}
%dir %{fe2basedir}/%{job_world}/%{scenario_job_dir}
%{fe2basedir}/%{job_world}/%{scenario_package}.zip
%dir %{fe2basedir}/%{job_world_pass}/%{scenario_dir}
%dir %{fe2basedir}/%{job_world_pass}/%{scenario_job_dir}

%files -n %{name}-%{agency}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1appsdir}/%{agency_world}
%{fe1appsdir}/%{agency_world}.war

%files -n %{name}-%{agency}-%{fe2}
%defattr(-,%{account},%{account_group})
%dir %{fe2appsdir}/%{agency_world}
%{fe2appsdir}/%{agency_world}.war

%changelog
* Tue Mar 20 2018 Sumie Satou <su-sato@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20180320173948
- update: gjp_conf_app_ver             20180320173948

* Mon Mar 19 2018 Sumie Satou <su-sato@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20180319175658
- update: gjp_conf_app_ver             20180319175658

* Wed Nov 1 2017 Sumie Satou <su-sato@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20171101181223
- update: gjp_conf_app_ver             20171101181223

* Tue Oct 11 2016 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_app_ver             20161011112035

* Wed Mar 9 2016 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20160208180313

* Thu Dec 17 2015  Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20151216172505

* Thu Nov 26 2015  Shigeru Hamamoto  <s-hamamoto@jprs.co.jp>
- update: JAVA_HOME /usr/local/jdk1.8/ 
- update: JAR_BIN   /usr/local/jdk1.8/bin/jar

* Mon Sep 1 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20140901140507
- update: gjp_conf_app_ver             20140901140507

* Thu Aug 21 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- add: gjp-tb-app-web-agent-web-pass

* Thu Mar 13 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20140313120739

* Fri Mar 7 2014 Masashi Hatakeyama <m-hatakeyama@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20140306215800
- update: gjp_conf_app_ver             20140306215800

* Fri Jan 18 2013 Tomohiro Nakagawa <t-nakagw@jprs.co.jp>
- update: gjp_conf_tomcat_ver          20130111184753
- update: gjp_conf_app_ver             20130111184753

* Thu Dec 13 2012  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gjp_conf_app_ver       20121212194938
- update: gjp_conf_app_internalweb_ver 20121212194938

* Fri Nov 9 2012  Atsushi Furuta  <furuta@jprs.co.jp>
- update: gjp_conf_tomcat_ver  20121109130634
- update: JAVA_HOME /usr/local/jdk1.6.0_37/ 
- update: JAR_BIN   /usr/local/jdk1.6.0_37/bin/jar

* Wed Mar 07 2012 k-kosuga <k-kosuga@jprs.co.jp>
- first release
