%define jar_path ./contact-gw/anonymous-web/target/%{profile}/
%define account       pasta0
%define account_group pasta0

%define appname       contact-proxy
%define fe1           f1
%define fe1basedir    /data/%{account}/
%define fe1appsdir    %{fe1basedir}/servlet/%{appname}/
%define fe1htdocs     %{fe1basedir}/htdocs/%{appname}/
%define acountlocal   /local/%{account}/servlet/%{appname}/

%define __jar_repack  %{nil}
%define debug_package %{nil}

%define MVN_BIN       /usr/local/maven3.6/bin/mvn

%bcond_with branch
%bcond_with real

%if %{with real} 
  %define profile   real
%else
  %define profile   jail
%endif

Name:     gtld-fe39-contact-proxy
Summary:  Anonymous contact g/w agency system
Version:  %{version}
Release:  %{release}
License:  Copyright(c) 2018 JPRS
Group:    Applications/Internet/Registrar

%description
%{summary}

%package -n %{name}-%{fe1}
Summary:  Anonymous contact g/w agency system for fe39

%description -n %{name}-%{fe1}
%{summary}



%prep
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT/*

%setup -T -c %{name}-%{release}

%if %{with branch}
TAG=`echo %{release} | %__sed -e 's/\./-/g'`
%else
TAG=`echo %{release}-%{version} | %__sed -e 's/\./-/g'`
%endif

git clone -b ${TAG} --single-branch --depth=1 http://git.sys.jprs.co.jp/shain-itaku/contact-gw.git

%build
export JAVA_HOME=/usr/local/jdk1.8/

pushd contact-gw/anonymous-project/
%{MVN_BIN} clean install
popd

pushd contact-gw/anonymous-common/
%{MVN_BIN} clean install -Dmaven.test.skip=true -P %{profile}
popd

pushd contact-gw/anonymous-web/
%{MVN_BIN} clean package -Dmaven.test.skip=true -P %{profile}
popd

%install

%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}
%__install -d ${RPM_BUILD_ROOT}%{fe1appsdir}/bin
%__install -p -m644 %{jar_path}*.jar      ${RPM_BUILD_ROOT}%{fe1appsdir}
%__install -d ${RPM_BUILD_ROOT}%{fe1htdocs}
pushd contact-gw/anonymous-web/bin/
%__install -p -m755 *.sh      ${RPM_BUILD_ROOT}%{fe1appsdir}/bin
popd
%__install -d ${RPM_BUILD_ROOT}%{acountlocal}
%__install -d ${RPM_BUILD_ROOT}%{acountlocal}/var
%__install -d ${RPM_BUILD_ROOT}%{acountlocal}/var/run
%__ln_s %{acountlocal}var ${RPM_BUILD_ROOT}%{fe1appsdir}/var

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT/*
[ "$RPM_BUILD_DIR" != "/" ] && rm -rf $RPM_BUILD_DIR/*


%files -n %{name}-%{fe1}
%defattr(-,%{account},%{account_group})
%dir %{fe1appsdir}
%dir %{fe1appsdir}/bin
%dir %{fe1htdocs}
%{fe1appsdir}*.jar
%{fe1appsdir}/bin/*.sh
%{fe1appsdir}/var
%dir %{acountlocal}
%dir %{acountlocal}/var/run

%changelog
* Mon Nov 26 2018 Yusuke Tokunaga <y-tokunaga@jprs.co.jp>
- Added htdocs files
* Wed Nov 07 2018 Yusuke Tokunaga <y-tokunaga@jprs.co.jp>
- This is the first release
