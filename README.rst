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
generated on Thursday 2024-05-02, 02:00:16
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

  | `40817 <https:////gerrit.fd.io/r/c/vpp/+/40817>`_ [VECR 6]: vlib: Add FreeBSD specific platform files
  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VECR 8]: ipsec: add SA validity check fetching IPsec SA
  | `40497 <https:////gerrit.fd.io/r/c/vpp/+/40497>`_ [VECR 22]: urpf: export to use it externally

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40763 <https:////gerrit.fd.io/r/c/vpp/+/40763>`_ [VECr 2]: acl: add missing byteswap header for musl

build: **Damjan Marion** <damarion@cisco.com>
  | `40851 <https:////gerrit.fd.io/r/c/vpp/+/40851>`_ [VECr 0]: dpdk: Don't depend on rdma-core on FreeBSD
  | `40849 <https:////gerrit.fd.io/r/c/vpp/+/40849>`_ [VECr 0]: dpdk: Use gnu sed on FreeBSD for header fix ups
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 2]: hs-test: added targets to makefiles to get coverage from HS tests

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `40660 <https:////gerrit.fd.io/r/c/vpp/+/40660>`_ [VECr 20]: cnat: add snat address dump

dev: **Damjan Marion** <damarion@cisco.com>
  | `40829 <https:////gerrit.fd.io/r/c/vpp/+/40829>`_ [VECr 5]: dev: fix mac address dump in trace output

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VECr 1]: docs: Restore and update nat section of progressive tutorial
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VECr 1]: docs: update core-pinning configuration
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 29]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `40853 <https:////gerrit.fd.io/r/c/vpp/+/40853>`_ [VECr 0]: dpdk: Only use --file-prefix flag on Linux
  | `40852 <https:////gerrit.fd.io/r/c/vpp/+/40852>`_ [VECr 0]: dpdk: Only reconfigure max pipe size on linux
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VECr 2]: vppinfra: fix dpdk compilation

fib: **Neale Ranns** <neale@graphiant.com>
  | `40705 <https:////gerrit.fd.io/r/c/vpp/+/40705>`_ [VECr 9]: fib: dvr dpo fix style
  | `40718 <https:////gerrit.fd.io/r/c/vpp/+/40718>`_ [VECr 12]: fib: set the value of the sw_if_index for DROP route
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 14]: fib: improve ipv6 fib scaling
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 15]: fib: fix udp encap mp-safe ops and id validation
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VECr 20]: fib: fix mpls tunnel restacking
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VECr 27]: fib: add ip4 fib preallocation support
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 29]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

gso: **Andrew Yourtchenko** <ayourtch@gmail.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 12]: gso: use the header offsets from buffer metadata

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 2]: hs-test: added targets to makefiles to get coverage from HS tests

iavf: **Damjan Marion** <damarion@cisco.com>
  | `40724 <https:////gerrit.fd.io/r/c/vpp/+/40724>`_ [VECr 0]: iavf: disable VLAN stripping when VLAN offload is set in caps

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VECr 0]: ikev2: multiple ts per profile

interface: **Dave Barach** <vpp@barachs.net>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 1]: fib: make mfib optional

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 1]: fib: make mfib optional
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VECr 2]: ip: add ip6 shallow reassembly output feature
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 2]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 2]: ip: fix ip4 shallow reassembly output feature handoff
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VECr 8]: ip: added CLI command to set ip6 reassembly params
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VECr 9]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 14]: fib: improve ipv6 fib scaling
  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VECr 16]: ip: discard old trace flag after copy
  | `40452 <https:////gerrit.fd.io/r/c/vpp/+/40452>`_ [VECr 19]: ip6: fix icmp error on check fail

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `40832 <https:////gerrit.fd.io/r/c/vpp/+/40832>`_ [VECr 2]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.
  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VECr 22]: ipsec: cli: 'set interface ipsec spd' support delete

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 7]: linux-cp: Add VRF synchronization

map: **Ole Troan** <ot@cisco.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 2]: ip: add extended shallow reassembly

marvell: **Damjan Marion** <damarion@cisco.com>
  | `40772 <https:////gerrit.fd.io/r/c/vpp/+/40772>`_ [VECr 9]: marvell: remove uses of uint

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 2]: ip: add extended shallow reassembly
  | `40487 <https:////gerrit.fd.io/r/c/vpp/+/40487>`_ [VECr 8]: urpf: allow per buffer fib
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 29]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `40761 <https:////gerrit.fd.io/r/c/vpp/+/40761>`_ [VECr 7]: nat: fix unitialized variable

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `40615 <https:////gerrit.fd.io/r/c/vpp/+/40615>`_ [VECr 1]: octeon: add support for vnet generic flow type
  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VECr 30]: octeon: add crypto framework

papi: **Ole Troan** <ot@cisco.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VECr 27]: papi: fix socket api max message id calculation

pci: **Damjan Marion** <damarion@cisco.com>
  | `40766 <https:////gerrit.fd.io/r/c/vpp/+/40766>`_ [VECr 7]: vlib: fix missing integer init

pg: **Dave Barach** <vpp@barachs.net>
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 12]: gso: use the header offsets from buffer metadata

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VECr 0]: tests: organize test coverage report generation
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 0]: tests: Added SRv6 End.Am behaviour test
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 1]: fib: make mfib optional
  | `40803 <https:////gerrit.fd.io/r/c/vpp/+/40803>`_ [VECr 1]: vlib: revert automatic core pinning changes
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 1]: vlib: fix automatic core pinning
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 2]: hs-test: added targets to makefiles to get coverage from HS tests
  | `40721 <https:////gerrit.fd.io/r/c/vpp/+/40721>`_ [VECr 6]: tests: minor improvements to test_snort
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 12]: gso: use the header offsets from buffer metadata
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 15]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 20]: fib: fix invalid udp encap id cases
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VECr 20]: fib: fix mpls tunnel restacking
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 29]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

udp: **Florin Coras** <fcoras@cisco.com>
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 15]: fib: fix udp encap mp-safe ops and id validation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 1]: fib: make mfib optional
  | `40762 <https:////gerrit.fd.io/r/c/vpp/+/40762>`_ [VECr 2]: tests: remove uses of uint
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 12]: gso: use the header offsets from buffer metadata
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 20]: fib: fix invalid udp encap id cases
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 29]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

urpf: **Neale Ranns** <neale@graphiant.com>
  | `40487 <https:////gerrit.fd.io/r/c/vpp/+/40487>`_ [VECr 8]: urpf: allow per buffer fib
  | `40703 <https:////gerrit.fd.io/r/c/vpp/+/40703>`_ [VECr 9]: urpf: node refacto

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 2]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40752 <https:////gerrit.fd.io/r/c/vpp/+/40752>`_ [VECr 1]: vlib: avoid pci scan without registrations
  | `40803 <https:////gerrit.fd.io/r/c/vpp/+/40803>`_ [VECr 1]: vlib: revert automatic core pinning changes
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 1]: vlib: fix automatic core pinning
  | `40759 <https:////gerrit.fd.io/r/c/vpp/+/40759>`_ [VECr 2]: vlib: fix use of RTLD_DEEPBIND for musl
  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VECr 12]: vppinfra: collect heap stats in constant time

vnet: **Damjan Marion** <damarion@cisco.com>
  | `40836 <https:////gerrit.fd.io/r/c/vpp/+/40836>`_ [VECr 2]: vnet: print Success for API errno 0 instead of UNKNOWN

vpp: **Dave Barach** <vpp@barachs.net>
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 1]: vlib: fix automatic core pinning
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 29]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40848 <https:////gerrit.fd.io/r/c/vpp/+/40848>`_ [VECr 0]: vlib: resolving core affinity on platforms with more than 128 cpus
  | `40803 <https:////gerrit.fd.io/r/c/vpp/+/40803>`_ [VECr 1]: vlib: revert automatic core pinning changes
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 1]: vlib: fix automatic core pinning
  | `40818 <https:////gerrit.fd.io/r/c/vpp/+/40818>`_ [VECr 6]: vppinfra: Include param.h on FreeBSD
  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VECr 12]: vppinfra: collect heap stats in constant time

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `40764 <https:////gerrit.fd.io/r/c/vpp/+/40764>`_ [VECr 2]: wireguard: use clib helpers for endianness
  | `40841 <https:////gerrit.fd.io/r/c/vpp/+/40841>`_ [VECr 2]: wireguard: fix uninitialized pointer read

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40722 <https:////gerrit.fd.io/r/c/vpp/+/40722>`_ [vEC 2]: tests: dns test improvements

**Alok Mishra** <almishra@marvell.com>:

  | `40669 <https:////gerrit.fd.io/r/c/vpp/+/40669>`_ [vEC 2]: octeon: add support for mac address update

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 69]: ipsec: notify key changes to crypto engine during sa update

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 133]: ena: add tx checksum offloads and tso support

**Benoît Ganne** <bganne@cisco.com>:

  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 77]: fib: log an error when destroying non-empty tables

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 133]: ebuild: adding libmemif to debian packages

**Dau Do** <daudo@yahoo.com>:

  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [vEC 4]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40503 <https:////gerrit.fd.io/r/c/vpp/+/40503>`_ [VeC 37]: tests: skip more excpuded plugin tests
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 37]: vlib: add config for elog tracing
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 117]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 133]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 134]: vppapigen: fix enum format function
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 146]: nat: fix det44 flaky test

**Elod Illes** <elod.illes@est.tech>:

  | `40571 <https:////gerrit.fd.io/r/c/vpp/+/40571>`_ [VEc 1]: docs: Use newer Ubuntu LTS in tutorial

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 84]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 131]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Fan Zhang** <fanzhang.oss@gmail.com>:

  | `40854 <https:////gerrit.fd.io/r/c/vpp/+/40854>`_ [vEC 0]: wireguard: fix dereference null return value

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 66]: session: make local port allocator fib aware

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 172]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 172]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 135]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 153]: interface: move set rss queues function

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 49]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [VEc 16]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [Vec 41]: ip: fix crash in ip4_neighbor_advertise

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40622 <https:////gerrit.fd.io/r/c/vpp/+/40622>`_ [VeC 33]: papi: more detailed packing error message
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 43]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [veC 60]: nat: add in2out-ip-fib-index config option

**Lajos Katona** <katonalala@gmail.com>:

  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [Vec 42]: docs: Add doc for API Trace Tools
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [Vec 49]: api: fix path for api definition files in vpe.api

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [vEC 7]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [VEc 9]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Maxime Peim** <mpeim@cisco.com>:

  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VeC 61]: fib: fix covered_inherit_add
  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 162]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `40719 <https:////gerrit.fd.io/r/c/vpp/+/40719>`_ [VEc 9]: ip: add support for drop route through vpp CLI
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 156]: geneve: add support for layer 3

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `40508 <https:////gerrit.fd.io/r/c/vpp/+/40508>`_ [VEc 27]: octeon: add support for Marvell Octeon9 SoC

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 44]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [vEC 29]: fib: Fix the make-before break load-balance construction
  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 70]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 73]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 176]: ip: IP address family common input node

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 134]: geneve: support custom options in decap

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [Vec 41]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 49]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Ole Troan** <otroan@employees.org>:

  | `40825 <https:////gerrit.fd.io/r/c/vpp/+/40825>`_ [VEc 1]: api: add to_net parameter to endian messages

**Pierre Pfister** <ppfister@cisco.com>:

  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vEc 2]: build: add config option for LD_PRELOAD

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VeC 32]: interface: check sw_if_index more thoroughly
  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VeC 47]: ikev2: handoff packets to main thread
  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VeC 68]: linux-cp: populate mapping vif-sw_if_index only for default-ns
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 86]: tap: add virtio polling option

**Todd Hsiao** <tohsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 56]: ip: Full reassembly and fragmentation enhancement

**Tom Jones** <thj@freebsd.org>:

  | `40468 <https:////gerrit.fd.io/r/c/vpp/+/40468>`_ [VEc 2]: vppinfra: Add platform cpu and domain get for FreeBSD

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VEc 7]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VEc 16]: vlib: mark cli quit command as mp_safe
  | `40415 <https:////gerrit.fd.io/r/c/vpp/+/40415>`_ [VEc 22]: ip: mark IP_ADDRESS_DUMP as mp-safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VEc 22]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 31]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 31]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 31]: stats: add sw interface tags to statseg
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 31]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 31]: mpls: fix crashes on mpls tunnel create/delete
  | `40438 <https:////gerrit.fd.io/r/c/vpp/+/40438>`_ [VeC 31]: vppinfra: fix mhash oob after unset and add tests
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 60]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 60]: nat: stick nat44-ed to use configured outside-fib

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 154]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 161]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VeC 68]: vppinfra: fix cpu freq init error if cpu support aperfmperf

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 40]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 49]: vppinfra: fix memory overrun in mhash_set_mem

**steven luong** <sluong@cisco.com>:

  | `40756 <https:////gerrit.fd.io/r/c/vpp/+/40756>`_ [vEC 1]: ethernet: check destination mac for L3 in ethernet-input node
  | `40576 <https:////gerrit.fd.io/r/c/vpp/+/40576>`_ [VeC 42]: virtio: Add RX queue full statisitics
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 83]: virtio: RSS support

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VEc 13]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process

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
authors          74
maintainers      56
committers       3
abandoned        0
================ ===

