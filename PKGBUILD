# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# See http://wiki.archlinux.org/index.php/Python_Package_Guidelines for more
# information on Python packaging.

# Maintainer: Jan Tuomi <jan-sebastian.tuomi@aalto.fi>
pkgname=python-sshmgr
pkgver=0.1
pkgrel=4
pkgdesc="Minimal ssh connection manager"
arch=('x86_64' 'i386')
url=""
license=('GPL')
groups=()
depends=('python3' 'screen')
makedepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
source=()
md5sums=()

package() {
  cd "$srcdir/$pkgname"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:

