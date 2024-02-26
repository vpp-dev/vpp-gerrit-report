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
generated on Monday 2024-02-26, 01:59:00
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

  | `40384 <https:////gerrit.fd.io/r/c/vpp/+/40384>`_ [VECR 0]: memif: don't include prctl.h

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VECr 2]: build: Connect FreeBSD system files to build

dev: **Damjan Marion** <damarion@cisco.com>
  | `40375 <https:////gerrit.fd.io/r/c/vpp/+/40375>`_ [VECr 2]: dev: add per-port vnet flow

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `40387 <https:////gerrit.fd.io/r/c/vpp/+/40387>`_ [VECr 2]: dhcp: Compare DIUD_LL as a network short

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 13]: dpdk: create and remove interface in runtime

fib: **Neale Ranns** <neale@graphiant.com>
  | `40368 <https:////gerrit.fd.io/r/c/vpp/+/40368>`_ [VECr 4]: fib: fix covered_inherit_add
  | `40237 <https:////gerrit.fd.io/r/c/vpp/+/40237>`_ [VECr 4]: fib: coverity 335348 out-of-bounds access
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 5]: ip: add support for buffer offload metadata in ip midchain
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 11]: fib: log an error when destroying non-empty tables

flowprobe: **Ole Troan** <otroan@employees.org>
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 12]: flowprobe: fix flush callbacks when multiple workers

interface: **Dave Barach** <vpp@barachs.net>
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 10]: interface: check sw_if_index more thoroughly

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 5]: ip: add support for buffer offload metadata in ip midchain
  | `40323 <https:////gerrit.fd.io/r/c/vpp/+/40323>`_ [VECr 13]: misc: fix icmp
  | `40294 <https:////gerrit.fd.io/r/c/vpp/+/40294>`_ [VECr 18]: ip: force full reassembly before virtual

ipip: **Ole Troan** <otroan@employees.org>
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 5]: ip: add support for buffer offload metadata in ip midchain

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 5]: ip: add support for buffer offload metadata in ip midchain

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `40379 <https:////gerrit.fd.io/r/c/vpp/+/40379>`_ [VECr 2]: linux-cp: populate mapping vif-sw_if_index only for default-ns
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 22]: linux-cp: Add VRF synchronization

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40373 <https:////gerrit.fd.io/r/c/vpp/+/40373>`_ [VECr 3]: crypto-sw-scheduler: crypto-dispatch improvement

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `39989 <https:////gerrit.fd.io/r/c/vpp/+/39989>`_ [VECr 4]: nat: add saddr info to nat44-ed o2i flow's rewrite

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `40376 <https:////gerrit.fd.io/r/c/vpp/+/40376>`_ [VECr 2]: octeon: add flow offload infra

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VECr 12]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

pnat: **Ole Troan** <ot@cisco.com>
  | `40385 <https:////gerrit.fd.io/r/c/vpp/+/40385>`_ [VECr 2]: nat: Include platform specific headers on FreeBSD

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 0]: session: make local port allocator fib aware

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VECr 20]: tap: add virtio polling option

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 0]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40058 <https:////gerrit.fd.io/r/c/vpp/+/40058>`_ [VECr 4]: tests: Added a simple prom(etheus exporter) plugin test
  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VECr 4]: tests: Added SRv6 End.Am behaviour test
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VECr 5]: ip: add support for buffer offload metadata in ip midchain
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 12]: flowprobe: fix flush callbacks when multiple workers
  | `40323 <https:////gerrit.fd.io/r/c/vpp/+/40323>`_ [VECr 13]: misc: fix icmp

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 0]: session: make local port allocator fib aware

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `39990 <https:////gerrit.fd.io/r/c/vpp/+/39990>`_ [VECr 5]: virtio: fix the packed ring support
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VECr 17]: virtio: RSS support
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VECr 20]: tap: add virtio polling option

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40393 <https:////gerrit.fd.io/r/c/vpp/+/40393>`_ [VECr 2]: vlib: Add calls to retrieve cpu and domain bitmaps on FreeBSD
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VECr 2]: build: Connect FreeBSD system files to build
  | `39992 <https:////gerrit.fd.io/r/c/vpp/+/39992>`_ [VECr 3]: vlib: fix counter_index check it need to check counter_index effectiveness with the commit 96158834db0, but it should be checked before addtion operation
  | `40353 <https:////gerrit.fd.io/r/c/vpp/+/40353>`_ [VECr 7]: build: Link agaist FREEBSD_LIBS

vpp: **Dave Barach** <vpp@barachs.net>
  | `40353 <https:////gerrit.fd.io/r/c/vpp/+/40353>`_ [VECr 7]: build: Link agaist FREEBSD_LIBS

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40377 <https:////gerrit.fd.io/r/c/vpp/+/40377>`_ [VECr 2]: vppinfra: fix cpu freq init error if cpu support aperfmperf
  | `40392 <https:////gerrit.fd.io/r/c/vpp/+/40392>`_ [VECr 2]: vppinfra: Add platform cpu and domain bitmap get functions
  | `40381 <https:////gerrit.fd.io/r/c/vpp/+/40381>`_ [VECr 2]: build: Connect FreeBSD system files to build
  | `40380 <https:////gerrit.fd.io/r/c/vpp/+/40380>`_ [VECr 2]: vppinfra: Add a platform specific system functions for FreeBSD
  | `40270 <https:////gerrit.fd.io/r/c/vpp/+/40270>`_ [VECr 27]: vppinfra: Link against lib execinfo on FreeBSD

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 172]: nat: nat44-ed get out2in workers failed for static mapping without port

**Adrian Villin** <avillin@cisco.com>:

  | `39988 <https:////gerrit.fd.io/r/c/vpp/+/39988>`_ [VEc 2]: hs-test: experimental support for multiple test instances
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VeC 41]: hs-test: added targets to makefiles to get coverage from HS tests

**Aman Singh** <aman.deep.singh@intel.com>:

  | `40371 <https:////gerrit.fd.io/r/c/vpp/+/40371>`_ [VEc 3]: ipsec: notify key changes to crypto engine during sa update

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 67]: ena: add tx checksum offloads and tso support

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 67]: ebuild: adding libmemif to debian packages

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [vEC 27]: misc: patch to test CI infra changes
  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VeC 40]: tests: organize test coverage report generation

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40149 <https:////gerrit.fd.io/r/c/vpp/+/40149>`_ [VEc 27]: vppinfra: fix mask compare and compress OOB reads
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 51]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 67]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 68]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 74]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 80]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [VEc 18]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 65]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Filip Tehlar** <ftehlar@cisco.com>:

  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [vec 37]: http: fix client receiving large data

**Florin Coras** <florin.coras@gmail.com>:

  | `40396 <https:////gerrit.fd.io/r/c/vpp/+/40396>`_ [vEC 0]: tcp: fix fin retransmit when out of buffers
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 117]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 106]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 106]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 69]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 87]: interface: move set rss queues function

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `39937 <https:////gerrit.fd.io/r/c/vpp/+/39937>`_ [VeC 52]: vlib: improve core pinning
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VeC 74]: misc: move lawful-intercept to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 143]: ip: fix crash in ip4_neighbor_advertise

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [vEC 12]: nat: add in2out-ip-fib-index config option

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 172]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 96]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 90]: geneve: add support for layer 3

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 136]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40360 <https:////gerrit.fd.io/r/c/vpp/+/40360>`_ [vEC 4]: vlib: Drain the frame queues before pausing at barrier.     - thread hand-off puts buffer in a frame queue between workers x and y. if worker y is waiting for the barrier lock, then these buffers are not processed until the lock is released. At that point state referred to by the buffers (e.g. an IPSec SA or an RX interface) could have been removed. so drain the frame queues for all workers before claiming to have reached the barrier.     - getting to the barrier is changed to a staged approach, with actions taken at each stage.
  | `40361 <https:////gerrit.fd.io/r/c/vpp/+/40361>`_ [vEC 7]: vlib: remove the now unrequired frame queue check count.    - there is now an accurate measure of whether frame queues are populated.
  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [vEC 21]: fib: Fix the make-before break load-balance construction    - ensure all DPOs are valid when used by workers. wait one loop for that as required.    - FIB UT to verify
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 110]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 177]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 177]: ip: Set the buffer error in ip6-input

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 68]: geneve: support custom options in decap

**Niyaz Murshed** <niyaz.murshed@arm.com>:

  | `40374 <https:////gerrit.fd.io/r/c/vpp/+/40374>`_ [VEc 1]: crypto: CLI to change dispatch mode

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 143]: l2: fix crash while sending traffic out orphan BVI

**Tom Jones** <thj@freebsd.org>:

  | `40390 <https:////gerrit.fd.io/r/c/vpp/+/40390>`_ [vEc 2]: tlsopenssl: Use EBADF on FreeBSD
  | `40388 <https:////gerrit.fd.io/r/c/vpp/+/40388>`_ [vEc 2]: hs_apps: Undef libepoll-shims close on FreeBSD
  | `40389 <https:////gerrit.fd.io/r/c/vpp/+/40389>`_ [VEc 2]: vcl: Only build vcl_ldpreload on Linux
  | `40394 <https:////gerrit.fd.io/r/c/vpp/+/40394>`_ [vEC 2]: vlib: Add vlib method for getting the current executable name
  | `40341 <https:////gerrit.fd.io/r/c/vpp/+/40341>`_ [vEC 2]: vlib: Add FreeBSD thread specific header and calls
  | `40386 <https:////gerrit.fd.io/r/c/vpp/+/40386>`_ [vEC 2]: tracedump: Add platform specific header on FreeBSD
  | `40383 <https:////gerrit.fd.io/r/c/vpp/+/40383>`_ [vEC 2]: acl: Add FreeBSD specific include to build

**Vladislav Grishenko** <themiron@mail.ru>:

  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 145]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 152]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 152]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 152]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 152]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 88]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 95]: vppapigen: recognize also _event as to_network
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 151]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 159]: ip-neighbor: add version 3 of neighbor event

**Wim de With** <wf@dewith.io>:

  | `40260 <https:////gerrit.fd.io/r/c/vpp/+/40260>`_ [vEC 23]: build: use GNUInstallDirs where possible

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 156]: interface dpdk avf: introducing setting RSS hash key feature

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 177]: af_xdp: optimizing send performance

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 165]: vrrp: dump vrrp vr peer

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [veC 33]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 113]: vppinfra: fix memory overrun in mhash_set_mem
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 123]: ping:mark ipv6 packets as locally originated

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VEc 3]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process

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
authors          64
maintainers      32
committers       1
abandoned        0
================ ===

