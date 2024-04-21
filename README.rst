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
generated on Sunday 2024-04-21, 02:02:39
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

  | `40497 <https:////gerrit.fd.io/r/c/vpp/+/40497>`_ [VECR 11]: urpf: export to use it externally
  | `40615 <https:////gerrit.fd.io/r/c/vpp/+/40615>`_ [VECR 24]: octeon: add support for vnet generic flow type
  | `40503 <https:////gerrit.fd.io/r/c/vpp/+/40503>`_ [VECR 26]: tests: skip more excpuded plugin tests

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

api: **Dave Barach** <vpp@barachs.net>
  | `40637 <https:////gerrit.fd.io/r/c/vpp/+/40637>`_ [VECr 5]: api: Add FreeBSD specific mechanisms for unix sockets

build: **Damjan Marion** <damarion@cisco.com>
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 9]: hs-test: added targets to makefiles to get coverage from HS tests
  | `40644 <https:////gerrit.fd.io/r/c/vpp/+/40644>`_ [VECr 9]: dpdk:  Disable building FreeBSD kernel modules

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `40660 <https:////gerrit.fd.io/r/c/vpp/+/40660>`_ [VECr 9]: cnat: add snat address dump

crypto-native: **Damjan Marion** <damarion@cisco.com>
  | `40545 <https:////gerrit.fd.io/r/c/vpp/+/40545>`_ [VECr 10]: crypto-native: add SHA2-HMAC

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `40633 <https:////gerrit.fd.io/r/c/vpp/+/40633>`_ [VECr 5]: docs: update core-pinning configuration
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 18]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `40640 <https:////gerrit.fd.io/r/c/vpp/+/40640>`_ [VECr 9]: dpdk: Only include vfio headers on linux
  | `40641 <https:////gerrit.fd.io/r/c/vpp/+/40641>`_ [VECr 9]: dpdk: Only use hugepage dir on Linux
  | `40642 <https:////gerrit.fd.io/r/c/vpp/+/40642>`_ [VECr 9]: dpdk: Only use vmbus on Linux
  | `40643 <https:////gerrit.fd.io/r/c/vpp/+/40643>`_ [VECr 9]: dpdk: Only require libnuma on Linux
  | `40645 <https:////gerrit.fd.io/r/c/vpp/+/40645>`_ [VECr 9]: dpdk: Only use vmbus on Linux
  | `40646 <https:////gerrit.fd.io/r/c/vpp/+/40646>`_ [VECr 9]: dpdk: Use FreeBSD specific values for network interface classes

fateshare: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 9]: vppinfra: Add method for getting current executable name
  | `40611 <https:////gerrit.fd.io/r/c/vpp/+/40611>`_ [VECr 25]: fateshare: Add FreeBSD specific API for controlling processes

fib: **Neale Ranns** <neale@graphiant.com>
  | `40719 <https:////gerrit.fd.io/r/c/vpp/+/40719>`_ [VECr 1]: ip: add support for drop route through vpp CLI
  | `40718 <https:////gerrit.fd.io/r/c/vpp/+/40718>`_ [VECr 1]: fib: set the value of the sw_if_index for DROP route
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 3]: fib: improve ipv6 fib scaling
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 4]: fib: fix udp encap mp-safe ops and id validation
  | `40705 <https:////gerrit.fd.io/r/c/vpp/+/40705>`_ [VECr 5]: fib: dvr dpo fix style
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VECr 9]: fib: fix mpls tunnel restacking
  | `40440 <https:////gerrit.fd.io/r/c/vpp/+/40440>`_ [VECr 16]: fib: add ip4 fib preallocation support
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 18]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VECr 20]: fib: ensure mpls dpo index is valid for its next node
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VECr 20]: fib: fix interface resolve from unlinked fib entries

gso: **Andrew Yourtchenko** <ayourtch@gmail.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 1]: gso: use the header offsets from buffer metadata

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 9]: hs-test: added targets to makefiles to get coverage from HS tests

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `40570 <https:////gerrit.fd.io/r/c/vpp/+/40570>`_ [VECr 2]: ikev2: uptime

interface: **Dave Barach** <vpp@barachs.net>
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 2]: fib: make mfib optional
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 20]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 20]: stats: add sw interface tags to statseg
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 21]: interface: check sw_if_index more thoroughly

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40719 <https:////gerrit.fd.io/r/c/vpp/+/40719>`_ [VECr 1]: ip: add support for drop route through vpp CLI
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 2]: fib: make mfib optional
  | `40745 <https:////gerrit.fd.io/r/c/vpp/+/40745>`_ [VECr 3]: fib: improve ipv6 fib scaling
  | `40717 <https:////gerrit.fd.io/r/c/vpp/+/40717>`_ [VECr 5]: ip: discard old trace flag after copy
  | `40452 <https:////gerrit.fd.io/r/c/vpp/+/40452>`_ [VECr 8]: ip6: fix icmp error on check fail

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `40750 <https:////gerrit.fd.io/r/c/vpp/+/40750>`_ [VECr 2]: dhcp: Update RA for prefixes inside DHCP-PD prefixes.
  | `40626 <https:////gerrit.fd.io/r/c/vpp/+/40626>`_ [VECr 19]: ip6-nd: simplify API to directly set options

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `40666 <https:////gerrit.fd.io/r/c/vpp/+/40666>`_ [VECr 11]: ipsec: cli: 'set interface ipsec spd' support delete

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 18]: linux-cp: Add VRF synchronization

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 18]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

mpls: **Neale Ranns** <neale@graphiant.com>
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 20]: mpls: fix crashes on mpls tunnel create/delete

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `39989 <https:////gerrit.fd.io/r/c/vpp/+/39989>`_ [VECr 13]: nat: add saddr info to nat44-ed o2i flow's rewrite

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `40753 <https:////gerrit.fd.io/r/c/vpp/+/40753>`_ [VECr 1]: octeon: add max packet length check
  | `40708 <https:////gerrit.fd.io/r/c/vpp/+/40708>`_ [VECr 5]: octeon: add support for SDP device
  | `40548 <https:////gerrit.fd.io/r/c/vpp/+/40548>`_ [VECr 19]: octeon: add crypto framework

papi: **Ole Troan** <ot@cisco.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `35726 <https:////gerrit.fd.io/r/c/vpp/+/35726>`_ [VECr 16]: papi: fix socket api max message id calculation
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 20]: stats: add sw interface tags to statseg
  | `40622 <https:////gerrit.fd.io/r/c/vpp/+/40622>`_ [VECr 22]: papi: more detailed packing error message

pci: **Damjan Marion** <damarion@cisco.com>
  | `40636 <https:////gerrit.fd.io/r/c/vpp/+/40636>`_ [VECr 5]: vlib: Place linux pci headers in a linux include block

pg: **Dave Barach** <vpp@barachs.net>
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 1]: gso: use the header offsets from buffer metadata
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 20]: stats: add interface link speed to statseg

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 1]: gso: use the header offsets from buffer metadata
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 2]: fib: make mfib optional
  | `40712 <https:////gerrit.fd.io/r/c/vpp/+/40712>`_ [VECr 2]: tests: allow to add remote hosts
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 4]: fib: fix udp encap mp-safe ops and id validation
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 4]: vlib: fix automatic core pinning
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 9]: fib: fix invalid udp encap id cases
  | `40697 <https:////gerrit.fd.io/r/c/vpp/+/40697>`_ [VECr 9]: fib: fix mpls tunnel restacking
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 9]: hs-test: added targets to makefiles to get coverage from HS tests
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 18]: tests: Added SRv6 End.Am behaviour test
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 18]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 20]: stats: add interface link speed to statseg
  | `40628 <https:////gerrit.fd.io/r/c/vpp/+/40628>`_ [VECr 20]: stats: add sw interface tags to statseg
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 20]: mpls: fix crashes on mpls tunnel create/delete

udp: **Florin Coras** <fcoras@cisco.com>
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 4]: fib: fix udp encap mp-safe ops and id validation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `36302 <https:////gerrit.fd.io/r/c/vpp/+/36302>`_ [VECr 1]: gso: use the header offsets from buffer metadata
  | `40746 <https:////gerrit.fd.io/r/c/vpp/+/40746>`_ [VECr 2]: fib: make mfib optional
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VECr 9]: fib: fix invalid udp encap id cases
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 18]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

urpf: **Neale Ranns** <neale@graphiant.com>
  | `40703 <https:////gerrit.fd.io/r/c/vpp/+/40703>`_ [VECr 5]: urpf: node refacto

vcl: **Florin Coras** <fcoras@cisco.com>
  | `40537 <https:////gerrit.fd.io/r/c/vpp/+/40537>`_ [VECr 15]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VECr 1]: vppinfra: collect heap stats in constant time
  | `40752 <https:////gerrit.fd.io/r/c/vpp/+/40752>`_ [VECr 1]: vlib: avoid pci scan without registrations
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 4]: vlib: fix automatic core pinning
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 9]: vppinfra: Add method for getting current executable name
  | `40629 <https:////gerrit.fd.io/r/c/vpp/+/40629>`_ [VECr 20]: stats: add interface link speed to statseg
  | `40478 <https:////gerrit.fd.io/r/c/vpp/+/40478>`_ [VECr 26]: vlib: add config for elog tracing

vpp: **Dave Barach** <vpp@barachs.net>
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 4]: vlib: fix automatic core pinning
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 9]: vppinfra: Add method for getting current executable name
  | `40488 <https:////gerrit.fd.io/r/c/vpp/+/40488>`_ [VECr 18]: bfd: move bfd to plugin, fix checkstyle, fix bfd test, bfd docs,

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [VECr 1]: vppinfra: collect heap stats in constant time
  | `40711 <https:////gerrit.fd.io/r/c/vpp/+/40711>`_ [VECr 4]: vlib: fix automatic core pinning
  | `40639 <https:////gerrit.fd.io/r/c/vpp/+/40639>`_ [VECr 9]: vppinfra: Add FreeBSD method for updating pmalloc lookup table
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [VECr 9]: vppinfra: Add method for getting current executable name
  | `40438 <https:////gerrit.fd.io/r/c/vpp/+/40438>`_ [VECr 20]: vppinfra: fix mhash oob after unset and add tests
  | `40392 <https:////gerrit.fd.io/r/c/vpp/+/40392>`_ [VECr 25]: vppinfra: Add platform cpu and domain bitmap get functions
  | `40270 <https:////gerrit.fd.io/r/c/vpp/+/40270>`_ [VECr 25]: vppinfra: Link against lib execinfo on FreeBSD

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [Vec 58]: ipsec: notify key changes to crypto engine during sa update

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 122]: ena: add tx checksum offloads and tso support

**Bence Romsics** <bence.romsics@gmail.com>:

  | `40402 <https:////gerrit.fd.io/r/c/vpp/+/40402>`_ [VeC 38]: docs: Restore and update nat section of progressive tutorial

**Benoît Ganne** <bganne@cisco.com>:

  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 66]: fib: log an error when destroying non-empty tables

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 122]: ebuild: adding libmemif to debian packages

**Dave Wallace** <dwallacelf@gmail.com>:

  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VeC 95]: tests: organize test coverage report generation

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 106]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 122]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 123]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 129]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 135]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [Vec 73]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 120]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Filip Tehlar** <filip.tehlar@gmail.com>:

  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [vec 92]: http: fix client receiving large data

**Florin Coras** <florin.coras@gmail.com>:

  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VeC 55]: session: make local port allocator fib aware
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 172]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 161]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 161]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 124]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 142]: interface: move set rss queues function

**Hadi Dernaika** <hadidernaika31@gmail.com>:

  | `39995 <https:////gerrit.fd.io/r/c/vpp/+/39995>`_ [Vec 38]: virtio: fix crash on show tun cli

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `40088 <https:////gerrit.fd.io/r/c/vpp/+/40088>`_ [VEc 5]: misc: move snap, llc, osi to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VEc 30]: ip: fix crash in ip4_neighbor_advertise

**Klement Sekera** <klement.sekera@gmail.com>:

  | `40547 <https:////gerrit.fd.io/r/c/vpp/+/40547>`_ [VeC 32]: vapi: don't store dict in length field

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [veC 49]: nat: add in2out-ip-fib-index config option

**Lajos Katona** <katonalala@gmail.com>:

  | `40471 <https:////gerrit.fd.io/r/c/vpp/+/40471>`_ [Vec 31]: docs: Add doc for API Trace Tools
  | `40460 <https:////gerrit.fd.io/r/c/vpp/+/40460>`_ [Vec 38]: api: fix path for api definition files in vpe.api

**Manual Praying** <bobobo1618@gmail.com>:

  | `40573 <https:////gerrit.fd.io/r/c/vpp/+/40573>`_ [vEC 2]: nat: Implement SNAT on hairpin NAT for TCP, UDP and ICMP.

**Maxime Peim** <mpeim@cisco.com>:

  | `40649 <https:////gerrit.fd.io/r/c/vpp/+/40649>`_ [VEc 2]: tests: allow ip table name
  | `40487 <https:////gerrit.fd.io/r/c/vpp/+/40487>`_ [vEc 4]: urpf: allow per buffer fib
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VeC 50]: fib: fix covered_inherit_add
  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 151]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 145]: geneve: add support for layer 3

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `40508 <https:////gerrit.fd.io/r/c/vpp/+/40508>`_ [VEc 16]: octeon: add support for Marvell Octeon9 SoC

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 33]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [vEC 18]: fib: Fix the make-before break load-balance construction
  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [veC 59]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [veC 62]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 165]: ip: IP address family common input node

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 123]: geneve: support custom options in decap

**Nikita Skrynnik** <nikita.skrynnik@xored.com>:

  | `40325 <https:////gerrit.fd.io/r/c/vpp/+/40325>`_ [VEc 30]: ping: Allow to specify a source interface in ping binary API
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VeC 38]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `40400 <https:////gerrit.fd.io/r/c/vpp/+/40400>`_ [VeC 36]: ikev2: handoff packets to main thread
  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VeC 57]: linux-cp: populate mapping vif-sw_if_index only for default-ns
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VeC 75]: tap: add virtio polling option

**Todd Hsiao** <tohsiao@cisco.com>:

  | `40462 <https:////gerrit.fd.io/r/c/vpp/+/40462>`_ [veC 45]: ip: Full reassembly and fragmentation enhancement

**Tom Jones** <thj@freebsd.org>:

  | `40341 <https:////gerrit.fd.io/r/c/vpp/+/40341>`_ [vEC 25]: vlib: Add FreeBSD thread specific header and calls
  | `40473 <https:////gerrit.fd.io/r/c/vpp/+/40473>`_ [vEC 25]: vlib: Add a skeleton pci interface for FreeBSD
  | `40469 <https:////gerrit.fd.io/r/c/vpp/+/40469>`_ [veC 44]: vlib: Use platform specific method to get exec name
  | `40470 <https:////gerrit.fd.io/r/c/vpp/+/40470>`_ [veC 44]: vpp: Add platform specific method to get exec name
  | `40468 <https:////gerrit.fd.io/r/c/vpp/+/40468>`_ [VeC 44]: vppinfra: Add platform cpu and domain get for FreeBSD
  | `40393 <https:////gerrit.fd.io/r/c/vpp/+/40393>`_ [Vec 51]: vlib: Add calls to retrieve cpu and domain bitmaps on FreeBSD
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VeC 57]: build: Connect FreeBSD system files to build
  | `40353 <https:////gerrit.fd.io/r/c/vpp/+/40353>`_ [VeC 62]: build: Link agaist FREEBSD_LIBS

**Vladislav Grishenko** <themiron@mail.ru>:

  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VEc 5]: vlib: mark cli quit command as mp_safe
  | `40415 <https:////gerrit.fd.io/r/c/vpp/+/40415>`_ [VEc 11]: ip: mark IP_ADDRESS_DUMP as mp-safe
  | `40436 <https:////gerrit.fd.io/r/c/vpp/+/40436>`_ [VEc 11]: ip: mark IP_TABLE_DUMP and IP_ROUTE_DUMP as mp-safe
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 49]: nat: fix nat44-ed address removal from fib
  | `40413 <https:////gerrit.fd.io/r/c/vpp/+/40413>`_ [VeC 49]: nat: stick nat44-ed to use configured outside-fib

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 143]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 150]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VeC 57]: vppinfra: fix cpu freq init error if cpu support aperfmperf

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [vEC 29]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 38]: vppinfra: fix memory overrun in mhash_set_mem
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 178]: ping:mark ipv6 packets as locally originated

**steven luong** <sluong@cisco.com>:

  | `40756 <https:////gerrit.fd.io/r/c/vpp/+/40756>`_ [vEC 0]: ethernet: check destination mac for L3 in ethernet-input node
  | `40576 <https:////gerrit.fd.io/r/c/vpp/+/40576>`_ [VeC 31]: virtio: Add RX queue full statisitics
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VeC 72]: virtio: RSS support

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VEc 2]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process

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
authors          69
maintainers      57
committers       3
abandoned        0
================ ===

