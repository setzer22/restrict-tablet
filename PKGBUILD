pkgname=restrict-tablet-git
pkgver=r3.30634ef
pkgrel=1
pkgdesc='Restrict your digital drawing pad or mouse to a screen region'
arch=('any')
url='https://github.com/setzer22/restrict-tablet'
license=('GPL3')
depends=('xorg-xrandr' 'xorg-xinput' 'slop') # 'python-pymatrix'
makedepends=('git')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
source=('restrict-tablet'::'git+https://github.com/setzer22/restrict-tablet.git')
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/${pkgname%-git}"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd "$srcdir/${pkgname%-git}"
}

package() {
    cd "$srcdir/${pkgname%-git}"
    mkdir -p "${pkgdir}/usr/bin/"
    mv "main.py" "${pkgdir}/usr/bin/restrict-tablet"
}
