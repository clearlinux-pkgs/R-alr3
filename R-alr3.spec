#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-alr3
Version  : 2.0.8
Release  : 11
URL      : https://cran.r-project.org/src/contrib/alr3_2.0.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/alr3_2.0.8.tar.gz
Summary  : Data to Accompany Applied Linear Regression 3rd Edition
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-car
BuildRequires : R-car
BuildRequires : buildreq-R

%description
'Applied Linear Regression,' 3rd edition, Wiley are presented.  
 This package depends on the car package. Many functions formerly 
 in alr3 have been renamed and now reside in car.  
 Data files have been lightly modified to make some data columns row labels.  Many 
 of these files are also in the newer alr4 package.

%prep
%setup -q -c -n alr3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552710116

%install
export SOURCE_DATE_EPOCH=1552710116
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library alr3
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library alr3
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library alr3
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  alr3 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/alr3/CITATION
/usr/lib64/R/library/alr3/DESCRIPTION
/usr/lib64/R/library/alr3/INDEX
/usr/lib64/R/library/alr3/Meta/Rd.rds
/usr/lib64/R/library/alr3/Meta/data.rds
/usr/lib64/R/library/alr3/Meta/features.rds
/usr/lib64/R/library/alr3/Meta/hsearch.rds
/usr/lib64/R/library/alr3/Meta/links.rds
/usr/lib64/R/library/alr3/Meta/nsInfo.rds
/usr/lib64/R/library/alr3/Meta/package.rds
/usr/lib64/R/library/alr3/NAMESPACE
/usr/lib64/R/library/alr3/R/alr3
/usr/lib64/R/library/alr3/R/alr3.rdb
/usr/lib64/R/library/alr3/R/alr3.rdx
/usr/lib64/R/library/alr3/data/Rdata.rdb
/usr/lib64/R/library/alr3/data/Rdata.rds
/usr/lib64/R/library/alr3/data/Rdata.rdx
/usr/lib64/R/library/alr3/extdata/BGSall.txt
/usr/lib64/R/library/alr3/extdata/BGSboys.txt
/usr/lib64/R/library/alr3/extdata/BGSgirls.txt
/usr/lib64/R/library/alr3/extdata/BigMac2003.txt
/usr/lib64/R/library/alr3/extdata/MWwords.txt
/usr/lib64/R/library/alr3/extdata/Mitchell.txt
/usr/lib64/R/library/alr3/extdata/UN1.txt
/usr/lib64/R/library/alr3/extdata/UN2.txt
/usr/lib64/R/library/alr3/extdata/UN3.txt
/usr/lib64/R/library/alr3/extdata/ais.txt
/usr/lib64/R/library/alr3/extdata/allshoots.txt
/usr/lib64/R/library/alr3/extdata/baeskel.txt
/usr/lib64/R/library/alr3/extdata/banknote.txt
/usr/lib64/R/library/alr3/extdata/blowAPB.txt
/usr/lib64/R/library/alr3/extdata/blowBF.txt
/usr/lib64/R/library/alr3/extdata/blowdown.txt
/usr/lib64/R/library/alr3/extdata/brains.txt
/usr/lib64/R/library/alr3/extdata/cakes.txt
/usr/lib64/R/library/alr3/extdata/cathedral.txt
/usr/lib64/R/library/alr3/extdata/caution.txt
/usr/lib64/R/library/alr3/extdata/challeng.txt
/usr/lib64/R/library/alr3/extdata/chloride.txt
/usr/lib64/R/library/alr3/extdata/cloud.txt
/usr/lib64/R/library/alr3/extdata/domedata.txt
/usr/lib64/R/library/alr3/extdata/domedata1.txt
/usr/lib64/R/library/alr3/extdata/donner.txt
/usr/lib64/R/library/alr3/extdata/downer.txt
/usr/lib64/R/library/alr3/extdata/drugcost.txt
/usr/lib64/R/library/alr3/extdata/dwaste.txt
/usr/lib64/R/library/alr3/extdata/florida.txt
/usr/lib64/R/library/alr3/extdata/forbes.txt
/usr/lib64/R/library/alr3/extdata/ftcollinssnow.txt
/usr/lib64/R/library/alr3/extdata/fuel2001.txt
/usr/lib64/R/library/alr3/extdata/galapagos.txt
/usr/lib64/R/library/alr3/extdata/galtonpeas.txt
/usr/lib64/R/library/alr3/extdata/heights.txt
/usr/lib64/R/library/alr3/extdata/highway.txt
/usr/lib64/R/library/alr3/extdata/hooker.txt
/usr/lib64/R/library/alr3/extdata/htwt.txt
/usr/lib64/R/library/alr3/extdata/jevons.txt
/usr/lib64/R/library/alr3/extdata/lakemary.txt
/usr/lib64/R/library/alr3/extdata/lakes.txt
/usr/lib64/R/library/alr3/extdata/landrent.txt
/usr/lib64/R/library/alr3/extdata/lathe1.txt
/usr/lib64/R/library/alr3/extdata/longshoots.txt
/usr/lib64/R/library/alr3/extdata/mantel.txt
/usr/lib64/R/library/alr3/extdata/mile.txt
/usr/lib64/R/library/alr3/extdata/npdata.txt
/usr/lib64/R/library/alr3/extdata/oldfaith.txt
/usr/lib64/R/library/alr3/extdata/physics.txt
/usr/lib64/R/library/alr3/extdata/physics1.txt
/usr/lib64/R/library/alr3/extdata/pipeline.txt
/usr/lib64/R/library/alr3/extdata/prodscore.txt
/usr/lib64/R/library/alr3/extdata/rat.txt
/usr/lib64/R/library/alr3/extdata/salary.txt
/usr/lib64/R/library/alr3/extdata/salarygov.txt
/usr/lib64/R/library/alr3/extdata/segreg.txt
/usr/lib64/R/library/alr3/extdata/shocks.txt
/usr/lib64/R/library/alr3/extdata/shortshoots.txt
/usr/lib64/R/library/alr3/extdata/sleep1.txt
/usr/lib64/R/library/alr3/extdata/snake.txt
/usr/lib64/R/library/alr3/extdata/sniffer.txt
/usr/lib64/R/library/alr3/extdata/snowgeese.txt
/usr/lib64/R/library/alr3/extdata/stopping.txt
/usr/lib64/R/library/alr3/extdata/swan96.txt
/usr/lib64/R/library/alr3/extdata/titanic.txt
/usr/lib64/R/library/alr3/extdata/torda.R
/usr/lib64/R/library/alr3/extdata/transact.txt
/usr/lib64/R/library/alr3/extdata/turk0.txt
/usr/lib64/R/library/alr3/extdata/turkey.txt
/usr/lib64/R/library/alr3/extdata/twins.txt
/usr/lib64/R/library/alr3/extdata/ufc.txt
/usr/lib64/R/library/alr3/extdata/ufcdf.txt
/usr/lib64/R/library/alr3/extdata/ufcgf.txt
/usr/lib64/R/library/alr3/extdata/ufcwc.txt
/usr/lib64/R/library/alr3/extdata/walleye.txt
/usr/lib64/R/library/alr3/extdata/water.txt
/usr/lib64/R/library/alr3/extdata/wblake.txt
/usr/lib64/R/library/alr3/extdata/wblake2.txt
/usr/lib64/R/library/alr3/extdata/wm1.txt
/usr/lib64/R/library/alr3/extdata/wm2.txt
/usr/lib64/R/library/alr3/extdata/wm3.txt
/usr/lib64/R/library/alr3/extdata/wm4.txt
/usr/lib64/R/library/alr3/extdata/wool.txt
/usr/lib64/R/library/alr3/help/AnIndex
/usr/lib64/R/library/alr3/help/aliases.rds
/usr/lib64/R/library/alr3/help/alr3.rdb
/usr/lib64/R/library/alr3/help/alr3.rdx
/usr/lib64/R/library/alr3/help/paths.rds
/usr/lib64/R/library/alr3/html/00Index.html
/usr/lib64/R/library/alr3/html/R.css
