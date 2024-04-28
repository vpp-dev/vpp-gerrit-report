#################
VPP-GERRIT-REPORT
#################

VPP Gerrit Report categorizes the state of the gerrit.fd.io review queue.  Each gerrit change is labeled with the following status:

========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - No unresolved comments
    - Review incomplete (Code-Review < +1)
    - 23 days since last update

The report generator sorts the gerrit changes into three categories based on the state and the person or group required to perform the next action:

- Committers:
  Status [VECR xx]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & approved by a maintainer.
  Action: A committer should do a final review and submit the change or provide comment(s).

- Maintainers:
  Status [VECr]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & not reviewed
  Action: The Maintainer should do a code review

- Authors:
  Status <other>: Gerrit Changes that are either not verified, expired, or comments not resolved
  Action: Author should rebase the change, fix verification errors, and/or resolve comments to move the status to [VECr]# Gerrit open patches processing tool

Here is the latest VPP Gerrit Report:
-------------------------------------

==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Sunday 2024-04-28, 02:04:39
--------------------------------------------


Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Committers:
-----------
| **These gerrit changes have been**

    - Verified
    - Not expired
    - Comments resolved
    - Approved by Maintainers

| **Please perform a final review & submit.**

  | `40817 <https:////gerrit.fd.io/r/c/vpp/+/40817>`_ [VECR 2]: vlib: Add FreeBSD specific platform files
  | `40788 <https:////gerrit.fd.io/r/c/vpp/+/40788>`_ [VECR 2]: octeon: fix roc_nix_npc_mac_addr_get() return value check
  | `40764 <https:////gerrit.fd.io/r/c/vpp/+/40764>`_ [VECR 4]: wireguard: use clib helpers for endianness
  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VECR 4]: ipsec: add SA validity check fetching IPsec SA
  | `40765 <https:////gerrit.fd.io/r/c/vpp/+/40765>`_ [VECR 5]: pci: fix missing limits.h
  | `40759 <https:////gerrit.fd.io/r/c/vpp/+/40759>`_ [VECR 5]: vlib: fix use of RTLD_DEEPBIND for musl
  | `40497 <https:////gerrit.fd.io/r/c/vpp/+/40497>`_ [VECR 18]: urpf: export to use it externally

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40763 <https:////gerrit.fd.io/r/c/vpp/+/40763>`_ [VECr 5]: acl: add missing byteswap header for musl

build: **Damjan Marion** <damarion@cisco.com>
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 16]: hs-test: added targets to makefiles to get coverage from HS tests

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `40660 <https:////gerrit.fd.io/r/c/vpp/+/40660>`_ [VECr 16]: cnat: add snat address dump

crypto-native: **Damjan Marion** <damarion@cisco.com>
  | `40545 <https:////gerrit.fd.io/r/c/vpp/+/40545>`_ [VECr 17]: crypto-native: add SHA2-HMAC

dev: **Damjan Marion** <damarion@cisco.com>
  | `40829 <https:////gerrit.fd.io/r/c/vpp/+/40829>`_ [VECr 1]: dev: fix mac address dump in trace output

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40571 <https:////gerrit.fd.io/r/c/vpp/+/40571>`_ [VECr 1]: docs: Use newer Ubuntu LTS in tutorial
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VECr 12]: docs: update core-pinning configuration
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 25]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VECr 5]: vppinfra: fix dpdk compilation

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40756 <https:////gerrit.fd.io/r/c/vpp/+/40756>`_ [VECr 4]: ethernet: check destination mac for L3 in ethernet-input node

fib: **Neale Ranns** <neale@graphiant.com>
  | `40705 <https:////gerrit.fd.io/r/c/vpp/+/40705>`_ [VECr 5]: fib: dvr dpo fix style
  | `40718 <https:////gerrit.fd.io/r/c/vpp/+/40718>`_ [VECr 8]: fib: set the value of the sw_if_index for DROP route
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 10]: fib: improve ipv6 fib scaling
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 11]: fib: fix udp encap mp-safe ops and id validation
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VECr 16]: fib: fix mpls tunnel restacking
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VECr 23]: fib: add ip4 fib preallocation support
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 25]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VECr 27]: fib: ensure mpls dpo index is valid for its next node
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VECr 27]: fib: fix interface resolve from unlinked fib entries

gso: **Andrew Yourtchenko** <ayourtch@gmail.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 8]: gso: use the header offsets from buffer metadata

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 16]: hs-test: added targets to makefiles to get coverage from HS tests

interface: **Dave Barach** <vpp@barachs.net>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 3]: fib: make mfib optional
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 27]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 27]: stats: add sw interface tags to statseg
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 28]: interface: check sw_if_index more thoroughly

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 3]: fib: make mfib optional
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VECr 4]: ip: added CLI command to set ip6 reassembly params
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VECr 5]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 10]: fib: improve ipv6 fib scaling
  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VECr 12]: ip: discard old trace flag after copy
  | `40452 <https:////gerrit.fd.io/r/c/vpp/+/40452>`_ [VECr 15]: ip6: fix icmp error on check fail

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VECr 18]: ipsec: cli: 'set interface ipsec spd' support delete

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 3]: linux-cp: Add VRF synchronization

marvell: **Damjan Marion** <damarion@cisco.com>
  | `40772 <https:////gerrit.fd.io/r/c/vpp/+/40772>`_ [VECr 5]: marvell: remove uses of uint

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40487 <https:////gerrit.fd.io/r/c/vpp/+/40487>`_ [VECr 4]: urpf: allow per buffer fib
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 25]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

mpls: **Neale Ranns** <neale@graphiant.com>
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 27]: mpls: fix crashes on mpls tunnel create/delete

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `40761 <https:////gerrit.fd.io/r/c/vpp/+/40761>`_ [VECr 3]: nat: fix unitialized variable

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `40753 <https:////gerrit.fd.io/r/c/vpp/+/40753>`_ [VECr 2]: octeon: add max packet length check
  | `40792 <https:////gerrit.fd.io/r/c/vpp/+/40792>`_ [VECr 2]: octeon: fix buffer free for more than 6 segment
  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VECr 26]: octeon: add crypto framework

papi: **Ole Troan** <ot@cisco.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VECr 23]: papi: fix socket api max message id calculation
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 27]: stats: add sw interface tags to statseg
  | `40622 <https:////gerrit.fd.io/r/c/vpp/+/40622>`_ [VECr 29]: papi: more detailed packing error message

pci: **Damjan Marion** <damarion@cisco.com>
  | `40766 <https:////gerrit.fd.io/r/c/vpp/+/40766>`_ [VECr 3]: vlib: fix missing integer init

pg: **Dave Barach** <vpp@barachs.net>
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 8]: gso: use the header offsets from buffer metadata
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 27]: stats: add interface link speed to statseg

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40721 <https:////gerrit.fd.io/r/c/vpp/+/40721>`_ [VECr 2]: tests: minor improvements to test_snort
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 3]: fib: make mfib optional
  | `40756 <https:////gerrit.fd.io/r/c/vpp/+/40756>`_ [VECr 4]: ethernet: check destination mac for L3 in ethernet-input node
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 8]: gso: use the header offsets from buffer metadata
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 11]: fib: fix udp encap mp-safe ops and id validation
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 11]: vlib: fix automatic core pinning
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 16]: fib: fix invalid udp encap id cases
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VECr 16]: fib: fix mpls tunnel restacking
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 16]: hs-test: added targets to makefiles to get coverage from HS tests
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 25]: tests: Added SRv6 End.Am behaviour test
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 25]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 27]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 27]: stats: add sw interface tags to statseg
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 27]: mpls: fix crashes on mpls tunnel create/delete

udp: **Florin Coras** <fcoras@cisco.com>
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 11]: fib: fix udp encap mp-safe ops and id validation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 3]: fib: make mfib optional
  | `40762 <https:////gerrit.fd.io/r/c/vpp/+/40762>`_ [VECr 5]: tests: remove uses of uint
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 8]: gso: use the header offsets from buffer metadata
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 16]: fib: fix invalid udp encap id cases
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 25]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

urpf: **Neale Ranns** <neale@graphiant.com>
  | `40487 <https:////gerrit.fd.io/r/c/vpp/+/40487>`_ [VECr 4]: urpf: allow per buffer fib
  | `40703 <https:////gerrit.fd.io/r/c/vpp/+/40703>`_ [VECr 5]: urpf: node refacto

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 5]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40752 <https:////gerrit.fd.io/r/c/vpp/+/40752>`_ [VECr 5]: vlib: avoid pci scan without registrations
  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VECr 8]: vppinfra: collect heap stats in constant time
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 11]: vlib: fix automatic core pinning
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 27]: stats: add interface link speed to statseg

vpp: **Dave Barach** <vpp@barachs.net>
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 11]: vlib: fix automatic core pinning
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 25]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40818 <https:////gerrit.fd.io/r/c/vpp/+/40818>`_ [VECr 2]: vppinfra: Include param.h on FreeBSD
  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VECr 8]: vppinfra: collect heap stats in constant time
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 11]: vlib: fix automatic core pinning
  | `40438 <https:////gerrit.fd.io/r/c/vpp/+/40438>`_ [VECr 27]: vppinfra: fix mhash oob after unset and add tests

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40722 <https:////gerrit.fd.io/r/c/vpp/+/40722>`_ [vEC 1]: tests: dns test improvements

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 65]: ipsec: notify key changes to crypto engine during sa update

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 129]: ena: add tx checksum offloads and tso support

**Bence Romsics** <bence.romsics@gmail.com>:

  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 45]: docs: Restore and update nat section of progressive tutorial

**Benoît Ganne** <bganne@cisco.com>:

  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 73]: fib: log an error when destroying non-empty tables

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 129]: ebuild: adding libmemif to debian packages

**Dau Do** <daudo@yahoo.com>:

  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [vEC 0]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dave Wallace** <dwallacelf@gmail.com>:

  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VeC 102]: tests: organize test coverage report generation

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40503 <https:////gerrit.fd.io/r/c/vpp/+/40503>`_ [VeC 33]: tests: skip more excpuded plugin tests
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 33]: vlib: add config for elog tracing
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 113]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 129]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 130]: vppapigen: fix enum format function
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 142]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 80]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 127]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [VEc 2]: http: fix client receiving large data

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 62]: session: make local port allocator fib aware
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 179]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 168]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 168]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 131]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 149]: interface: move set rss queues function

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 45]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [VEc 12]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [Vec 37]: ip: fix crash in ip4_neighbor_advertise

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 39]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [veC 56]: nat: add in2out-ip-fib-index config option

**Lajos Katona** <katonalala@gmail.com>:

  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [Vec 38]: docs: Add doc for API Trace Tools
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [Vec 45]: api: fix path for api definition files in vpe.api

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [vEC 3]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [VEc 5]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Maxime Peim** <mpeim@cisco.com>:

  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VeC 57]: fib: fix covered_inherit_add
  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 158]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `40719 <https:////gerrit.fd.io/r/c/vpp/+/40719>`_ [VEc 5]: ip: add support for drop route through vpp CLI
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 152]: geneve: add support for layer 3

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `40508 <https:////gerrit.fd.io/r/c/vpp/+/40508>`_ [VEc 23]: octeon: add support for Marvell Octeon9 SoC

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 40]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [vEC 25]: fib: Fix the make-before break load-balance construction
  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 66]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 69]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 172]: ip: IP address family common input node

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 130]: geneve: support custom options in decap

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [Vec 37]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 45]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Ole Troan** <otroan@employees.org>:

  | `40825 <https:////gerrit.fd.io/r/c/vpp/+/40825>`_ [VEc 0]: api: add to_net parameter to endian messages

**Pierre Pfister** <ppfister@cisco.com>:

  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [VEc 5]: build: add config option for LD_PRELOAD

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VeC 43]: ikev2: handoff packets to main thread
  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VeC 64]: linux-cp: populate mapping vif-sw_if_index only for default-ns
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 82]: tap: add virtio polling option

**Todd Hsiao** <tohsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 52]: ip: Full reassembly and fragmentation enhancement

**Tom Jones** <thj@freebsd.org>:

  | `40468 <https:////gerrit.fd.io/r/c/vpp/+/40468>`_ [VEc 3]: vppinfra: Add platform cpu and domain get for FreeBSD

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VEc 3]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VEc 12]: vlib: mark cli quit command as mp_safe
  | `40415 <https:////gerrit.fd.io/r/c/vpp/+/40415>`_ [VEc 18]: ip: mark IP_ADDRESS_DUMP as mp-safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VEc 18]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 56]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 56]: nat: stick nat44-ed to use configured outside-fib

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 150]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 157]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VeC 64]: vppinfra: fix cpu freq init error if cpu support aperfmperf

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 36]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 45]: vppinfra: fix memory overrun in mhash_set_mem

**sriram vatala** <svatala@marvell.com>:

  | `40615 <https:////gerrit.fd.io/r/c/vpp/+/40615>`_ [vEC 4]: octeon: add support for vnet generic flow type

**steven luong** <sluong@cisco.com>:

  | `40576 <https:////gerrit.fd.io/r/c/vpp/+/40576>`_ [VeC 38]: virtio: Add RX queue full statisitics
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 79]: virtio: RSS support

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VEc 9]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process

Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Statistics:
-----------
================ ===
Patches assigned
================ ===
authors          67
maintainers      50
committers       7
abandoned        0
================ ===

