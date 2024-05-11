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
generated on Saturday 2024-05-11, 01:59:58
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

  | `40703 <https:////gerrit.fd.io/r/c/vpp/+/40703>`_ [VECR 4]: urpf: node refacto

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

build: **Damjan Marion** <damarion@cisco.com>
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 11]: hs-test: added targets to makefiles to get coverage from HS tests

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `40660 <https:////gerrit.fd.io/r/c/vpp/+/40660>`_ [VECr 29]: cnat: add snat address dump

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40866 <https:////gerrit.fd.io/r/c/vpp/+/40866>`_ [VECr 3]: sr: move srmpls to a plugin
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VECr 8]: docs: update core-pinning configuration
  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VECr 10]: docs: Restore and update nat section of progressive tutorial

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `40760 <https:////gerrit.fd.io/r/c/vpp/+/40760>`_ [VECr 3]: vppinfra: fix dpdk compilation
  | `40873 <https:////gerrit.fd.io/r/c/vpp/+/40873>`_ [VECr 3]: dpdk: Only prealloc huge pages on Linux

fib: **Neale Ranns** <neale@graphiant.com>
  | `40705 <https:////gerrit.fd.io/r/c/vpp/+/40705>`_ [VECr 4]: fib: dvr dpo fix style
  | `40718 <https:////gerrit.fd.io/r/c/vpp/+/40718>`_ [VECr 21]: fib: set the value of the sw_if_index for DROP route
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 23]: fib: improve ipv6 fib scaling
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 24]: fib: fix udp encap mp-safe ops and id validation
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VECr 29]: fib: fix mpls tunnel restacking

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `40881 <https:////gerrit.fd.io/r/c/vpp/+/40881>`_ [VECr 0]: http: fix server sending all status codes
  | `40729 <https:////gerrit.fd.io/r/c/vpp/+/40729>`_ [VECr 0]: hs-test: fixed timed out tests passing in the CI
  | `40727 <https:////gerrit.fd.io/r/c/vpp/+/40727>`_ [VECr 0]: hs-test: break TcpWithLoss (unstable)
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 11]: hs-test: added targets to makefiles to get coverage from HS tests

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `40881 <https:////gerrit.fd.io/r/c/vpp/+/40881>`_ [VECr 0]: http: fix server sending all status codes

http: **Florin Coras** <fcoras@cisco.com>
  | `40881 <https:////gerrit.fd.io/r/c/vpp/+/40881>`_ [VECr 0]: http: fix server sending all status codes

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `40850 <https:////gerrit.fd.io/r/c/vpp/+/40850>`_ [VECr 8]: ikev2: multiple ts per profile

interface: **Dave Barach** <vpp@barachs.net>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 8]: fib: make mfib optional

ioam: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VECr 0]: build: don't embed directives within macro arguments

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40879 <https:////gerrit.fd.io/r/c/vpp/+/40879>`_ [VECr 0]: build: don't embed directives within macro arguments
  | `40720 <https:////gerrit.fd.io/r/c/vpp/+/40720>`_ [VECr 8]: ip: added CLI command to set ip6 reassembly params
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 8]: fib: make mfib optional
  | `40838 <https:////gerrit.fd.io/r/c/vpp/+/40838>`_ [VECr 11]: ip: add ip6 shallow reassembly output feature
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 11]: ip: add extended shallow reassembly
  | `40837 <https:////gerrit.fd.io/r/c/vpp/+/40837>`_ [VECr 11]: ip: fix ip4 shallow reassembly output feature handoff
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VECr 18]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 23]: fib: improve ipv6 fib scaling
  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VECr 25]: ip: discard old trace flag after copy
  | `40452 <https:////gerrit.fd.io/r/c/vpp/+/40452>`_ [VECr 28]: ip6: fix icmp error on check fail

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `40767 <https:////gerrit.fd.io/r/c/vpp/+/40767>`_ [VECr 2]: ipsec: add SA validity check fetching IPsec SA
  | `40832 <https:////gerrit.fd.io/r/c/vpp/+/40832>`_ [VECr 11]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 16]: linux-cp: Add VRF synchronization

map: **Ole Troan** <ot@cisco.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 11]: ip: add extended shallow reassembly

marvell: **Damjan Marion** <damarion@cisco.com>
  | `40772 <https:////gerrit.fd.io/r/c/vpp/+/40772>`_ [VECr 8]: marvell: remove uses of uint

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40866 <https:////gerrit.fd.io/r/c/vpp/+/40866>`_ [VECr 3]: sr: move srmpls to a plugin
  | `40875 <https:////gerrit.fd.io/r/c/vpp/+/40875>`_ [VECr 3]: netmap: Reinstate and update netmap plugin
  | `40497 <https:////gerrit.fd.io/r/c/vpp/+/40497>`_ [VECr 4]: urpf: export to use it externally
  | `40839 <https:////gerrit.fd.io/r/c/vpp/+/40839>`_ [VECr 11]: ip: add extended shallow reassembly

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `40761 <https:////gerrit.fd.io/r/c/vpp/+/40761>`_ [VECr 2]: nat: fix unitialized variable

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `40669 <https:////gerrit.fd.io/r/c/vpp/+/40669>`_ [VECr 3]: octeon: add support for mac address update

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40503 <https:////gerrit.fd.io/r/c/vpp/+/40503>`_ [VECr 0]: tests: skip more excluded plugin tests
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 8]: vlib: fix automatic core pinning
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 8]: fib: make mfib optional
  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VECr 9]: tests: organize test coverage report generation
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 9]: tests: Added SRv6 End.Am behaviour test
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 11]: hs-test: added targets to makefiles to get coverage from HS tests
  | `40721 <https:////gerrit.fd.io/r/c/vpp/+/40721>`_ [VECr 15]: tests: minor improvements to test_snort
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 24]: fib: fix udp encap mp-safe ops and id validation
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 29]: fib: fix invalid udp encap id cases
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VECr 29]: fib: fix mpls tunnel restacking

udp: **Florin Coras** <fcoras@cisco.com>
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 24]: fib: fix udp encap mp-safe ops and id validation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 8]: fib: make mfib optional
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 29]: fib: fix invalid udp encap id cases

vapi: **Ole Troan** <ot@cisco.com>
  | `40861 <https:////gerrit.fd.io/r/c/vpp/+/40861>`_ [VECr 6]: vapi: remove plugin dependency from tests

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 11]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 8]: vlib: fix automatic core pinning
  | `40752 <https:////gerrit.fd.io/r/c/vpp/+/40752>`_ [VECr 10]: vlib: avoid pci scan without registrations
  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VECr 21]: vppinfra: collect heap stats in constant time

vnet: **Damjan Marion** <damarion@cisco.com>
  | `40836 <https:////gerrit.fd.io/r/c/vpp/+/40836>`_ [VECr 11]: vnet: print Success for API errno 0 instead of UNKNOWN

vpp: **Dave Barach** <vpp@barachs.net>
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 8]: vlib: fix automatic core pinning

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 8]: vlib: fix automatic core pinning
  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VECr 21]: vppinfra: collect heap stats in constant time

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `40764 <https:////gerrit.fd.io/r/c/vpp/+/40764>`_ [VECr 3]: wireguard: use clib helpers for endianness
  | `40854 <https:////gerrit.fd.io/r/c/vpp/+/40854>`_ [VECr 8]: wireguard: fix dereference null return value
  | `40841 <https:////gerrit.fd.io/r/c/vpp/+/40841>`_ [VECr 11]: wireguard: fix uninitialized pointer read

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Villin** <avillin@cisco.com>:

  | `40728 <https:////gerrit.fd.io/r/c/vpp/+/40728>`_ [vEC 0]: hs-test: break VCL tests (timeout)
  | `40726 <https:////gerrit.fd.io/r/c/vpp/+/40726>`_ [vEC 0]: hs-test: breaks HttpCliTest
  | `40722 <https:////gerrit.fd.io/r/c/vpp/+/40722>`_ [vEC 8]: tests: dns test improvements

**Alok Mishra** <almishra@marvell.com>:

  | `40829 <https:////gerrit.fd.io/r/c/vpp/+/40829>`_ [VEc 4]: dev: fix mac address dump in trace output

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 78]: ipsec: notify key changes to crypto engine during sa update

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `39994 <https:////gerrit.fd.io/r/c/vpp/+/39994>`_ [vEc 2]: pvti: Packet Vector Tunnel Interface

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 142]: ena: add tx checksum offloads and tso support

**Benoît Ganne** <bganne@cisco.com>:

  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 86]: fib: log an error when destroying non-empty tables

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 142]: ebuild: adding libmemif to debian packages

**Dau Do** <daudo@yahoo.com>:

  | `40831 <https:////gerrit.fd.io/r/c/vpp/+/40831>`_ [vEC 13]: ipsec: added CLI command to show the SA's distributed between workers. Added configuration option to adjust the worker queue size. Both of these are used for performance tune-up. In our setting, it's best to set a bigger queue size to avoid the congestion drop. If not set, it's default to current queue size.

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VeC 46]: vlib: add config for elog tracing
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 126]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 142]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 143]: vppapigen: fix enum format function
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 155]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 93]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 140]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 75]: session: make local port allocator fib aware

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 144]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 162]: interface: move set rss queues function

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 58]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [VEc 25]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [Vec 50]: ip: fix crash in ip4_neighbor_advertise

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40622 <https:////gerrit.fd.io/r/c/vpp/+/40622>`_ [VeC 42]: papi: more detailed packing error message
  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 52]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [veC 69]: nat: add in2out-ip-fib-index config option

**Lajos Katona** <katonalala@gmail.com>:

  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [VEc 4]: api: Refresh VPP API language with path background
  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [VEc 4]: docs: Add doc for API Trace Tools

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [vEC 8]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [VEc 18]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.

**Maxime Peim** <mpeim@cisco.com>:

  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VeC 70]: fib: fix covered_inherit_add
  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 171]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `40719 <https:////gerrit.fd.io/r/c/vpp/+/40719>`_ [VEc 18]: ip: add support for drop route through vpp CLI
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 165]: geneve: add support for layer 3

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `40508 <https:////gerrit.fd.io/r/c/vpp/+/40508>`_ [VEc 7]: octeon: add support for Marvell Octeon9 SoC

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 53]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [veC 38]: fib: Fix the make-before break load-balance construction
  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 79]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 82]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 143]: geneve: support custom options in decap

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [Vec 50]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 58]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Nithinsen Kaithakadan** <nkaithakadan@marvell.com>:

  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VeC 39]: octeon: add crypto framework

**Oussama Drici** <o.drici@esi-sba.dz>:

  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VeC 38]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

**Pierre Pfister** <ppfister@cisco.com>:

  | `40758 <https:////gerrit.fd.io/r/c/vpp/+/40758>`_ [vEc 3]: build: add config option for LD_PRELOAD

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VeC 56]: ikev2: handoff packets to main thread
  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VeC 77]: linux-cp: populate mapping vif-sw_if_index only for default-ns
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 95]: tap: add virtio polling option

**Todd Hsiao** <tohsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [vEC 8]: ip: Full reassembly and fragmentation enhancement

**Tom Jones** <thj@freebsd.org>:

  | `40468 <https:////gerrit.fd.io/r/c/vpp/+/40468>`_ [VEc 3]: vppinfra: Add platform cpu and domain get for FreeBSD

**Vinod Krishna** <vinod.krishna@arm.com>:

  | `40848 <https:////gerrit.fd.io/r/c/vpp/+/40848>`_ [VEc 4]: vlib: resolving core affinity on platforms with more than 128 cpus

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VEc 1]: ip6-nd: simplify API to directly set options

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VEc 25]: vlib: mark cli quit command as mp_safe
  | `40415 <https:////gerrit.fd.io/r/c/vpp/+/40415>`_ [Vec 31]: ip: mark IP_ADDRESS_DUMP as mp-safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [Vec 31]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VeC 36]: fib: add ip4 fib preallocation support
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VeC 36]: papi: fix socket api max message id calculation
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 40]: fib: ensure mpls dpo index is valid for its next node
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VeC 40]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VeC 40]: stats: add sw interface tags to statseg
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 40]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 40]: mpls: fix crashes on mpls tunnel create/delete
  | `40438 <https:////gerrit.fd.io/r/c/vpp/+/40438>`_ [VeC 40]: vppinfra: fix mhash oob after unset and add tests
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 69]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 69]: nat: stick nat44-ed to use configured outside-fib

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 163]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 170]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VeC 31]: ipsec: cli: 'set interface ipsec spd' support delete
  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VeC 77]: vppinfra: fix cpu freq init error if cpu support aperfmperf

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 49]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 58]: vppinfra: fix memory overrun in mhash_set_mem

**sriram vatala** <svatala@marvell.com>:

  | `40615 <https:////gerrit.fd.io/r/c/vpp/+/40615>`_ [VEc 3]: octeon: add support for vnet generic flow type

**steven luong** <sluong@cisco.com>:

  | `40576 <https:////gerrit.fd.io/r/c/vpp/+/40576>`_ [VeC 51]: virtio: Add RX queue full statisitics
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 92]: virtio: RSS support

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VEc 22]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process

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
authors          75
maintainers      47
committers       1
abandoned        0
================ ===

