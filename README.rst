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
generated on Monday 2024-02-12, 01:57:31
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

  | `40250 <https:////gerrit.fd.io/r/c/vpp/+/40250>`_ [VECR 18]: af_packet : fix crash on interface creation

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `40291 <https:////gerrit.fd.io/r/c/vpp/+/40291>`_ [VECr 5]: buffers: bring back cache occupancy improvement

build: **Damjan Marion** <damarion@cisco.com>
  | `40248 <https:////gerrit.fd.io/r/c/vpp/+/40248>`_ [VECr 18]: build: Add FreeBSD as a supported platform for cmake
  | `40247 <https:////gerrit.fd.io/r/c/vpp/+/40247>`_ [VECr 18]: build: Limit external libraries on FreeBSD
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 27]: hs-test: added targets to makefiles to get coverage from HS tests

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `40046 <https:////gerrit.fd.io/r/c/vpp/+/40046>`_ [VECr 5]: wireguard: notify key changes to crypto engine

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `40047 <https:////gerrit.fd.io/r/c/vpp/+/40047>`_ [VECr 5]: crypto-openssl: refactor openssl API usage

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 21]: dpdk: create and remove interface in runtime

fib: **Neale Ranns** <neale@graphiant.com>
  | `40237 <https:////gerrit.fd.io/r/c/vpp/+/40237>`_ [VECr 11]: fib: coverity 335348 out-of-bounds access
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 30]: fib: log an error when destroying non-empty tables

flowprobe: **Ole Troan** <otroan@employees.org>
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 25]: flowprobe: fix flush callbacks when multiple workers

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 27]: hs-test: added targets to makefiles to get coverage from HS tests

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `40294 <https:////gerrit.fd.io/r/c/vpp/+/40294>`_ [VECr 4]: ip: force full reassembly before virtual
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VECr 30]: ip6: ECMP hash support for ipv6 fragments

ip_session_redirect: **Benoît Ganne** <bganne@cisco.com>
  | `40321 <https:////gerrit.fd.io/r/c/vpp/+/40321>`_ [VECr 3]: ip_session_redirect: export symbols

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 8]: linux-cp: Add VRF synchronization

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `40322 <https:////gerrit.fd.io/r/c/vpp/+/40322>`_ [VECr 3]: build: add fib configuring option
  | `40261 <https:////gerrit.fd.io/r/c/vpp/+/40261>`_ [VECr 13]: vnet:	Don't use __unused for struct padding

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `40246 <https:////gerrit.fd.io/r/c/vpp/+/40246>`_ [VECr 13]: ping: Check only PING_RESPONSE_IP4 and PING_RESPONSE_IP6 events

session: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 4]: session: make local port allocator fib aware

svm: **Dave Barach** <vpp@barachs.net>
  | `40274 <https:////gerrit.fd.io/r/c/vpp/+/40274>`_ [VECr 13]: svm: Add FreeBSD specific signal handling path
  | `40272 <https:////gerrit.fd.io/r/c/vpp/+/40272>`_ [VECr 13]: svm: Include stdint on FreeBSD

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VECr 6]: tap: add virtio polling option

tcp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 4]: session: make local port allocator fib aware

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `40283 <https:////gerrit.fd.io/r/c/vpp/+/40283>`_ [VECr 4]: tests: refactor virtual interface tests
  | `40144 <https:////gerrit.fd.io/r/c/vpp/+/40144>`_ [VECr 25]: flowprobe: fix flush callbacks when multiple workers
  | `40201 <https:////gerrit.fd.io/r/c/vpp/+/40201>`_ [VECr 26]: tests: organize test coverage report generation
  | `40177 <https:////gerrit.fd.io/r/c/vpp/+/40177>`_ [VECr 27]: hs-test: added targets to makefiles to get coverage from HS tests

udp: **Florin Coras** <fcoras@cisco.com>
  | `40287 <https:////gerrit.fd.io/r/c/vpp/+/40287>`_ [VECr 4]: session: make local port allocator fib aware
  | `40320 <https:////gerrit.fd.io/r/c/vpp/+/40320>`_ [VECr 4]: udp: unregister ports on all cleanups

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `40109 <https:////gerrit.fd.io/r/c/vpp/+/40109>`_ [VECr 3]: virtio: RSS support
  | `40292 <https:////gerrit.fd.io/r/c/vpp/+/40292>`_ [VECr 6]: tap: add virtio polling option

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `40252 <https:////gerrit.fd.io/r/c/vpp/+/40252>`_ [VECr 13]: vlib: Use platform specific headers for sched.h

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `40263 <https:////gerrit.fd.io/r/c/vpp/+/40263>`_ [VECr 13]: vppinfra: Don't build perfmon on FreeBSD
  | `40271 <https:////gerrit.fd.io/r/c/vpp/+/40271>`_ [VECr 13]: vppinfra: Provide FreeBSD implementation of clib_mem functions
  | `40273 <https:////gerrit.fd.io/r/c/vpp/+/40273>`_ [VECr 13]: vppinfra: Only prealloc hugepages on Linux
  | `40270 <https:////gerrit.fd.io/r/c/vpp/+/40270>`_ [VECr 13]: vppinfra: Link against lib execinfo on FreeBSD
  | `40269 <https:////gerrit.fd.io/r/c/vpp/+/40269>`_ [VECr 13]: vppinfra: Add a stubbed out test_perf function for FreeBSD
  | `40268 <https:////gerrit.fd.io/r/c/vpp/+/40268>`_ [VECr 13]: vppinfra: Make program counter printing more portable
  | `40267 <https:////gerrit.fd.io/r/c/vpp/+/40267>`_ [VECr 13]: vppinfra: Place SIGPWR behind a linux define
  | `40266 <https:////gerrit.fd.io/r/c/vpp/+/40266>`_ [VECr 13]: vppinfra: Add netlink header on FreeBSD
  | `40265 <https:////gerrit.fd.io/r/c/vpp/+/40265>`_ [VECr 13]: vppinfra: Protect Linux specific features behind CLIB_LINUX
  | `40264 <https:////gerrit.fd.io/r/c/vpp/+/40264>`_ [VECr 13]: vppinfra: MAP_HUGETLB isn't available on FreeBSD
  | `40262 <https:////gerrit.fd.io/r/c/vpp/+/40262>`_ [VECr 13]: vppinfra: Stub out get_current_cpu and get_current_numa on FreeBSD
  | `40251 <https:////gerrit.fd.io/r/c/vpp/+/40251>`_ [VECr 17]: vppinfra: Put clib_perf* behind Linux checks and provide stubs for FreeBSD

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 158]: nat: nat44-ed get out2in workers failed for static mapping without port

**Adrian Villin** <avillin@cisco.com>:

  | `40073 <https:////gerrit.fd.io/r/c/vpp/+/40073>`_ [VeC 62]: tests: Added SRv6 End.Am behaviour test
  | `40058 <https:////gerrit.fd.io/r/c/vpp/+/40058>`_ [VeC 62]: tests: Added a simple prom(etheus exporter) plugin test

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 13]: ip: add support for buffer offload metadata in ip midchain
  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [vec 53]: ena: add tx checksum offloads and tso support

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 53]: ebuild: adding libmemif to debian packages

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [vEC 13]: misc: patch to test CI infra changes

**Denys Haryachyy** <garyachy@gmail.com>:

  | `40257 <https:////gerrit.fd.io/r/c/vpp/+/40257>`_ [VEc 2]: ikev2: dump state and profile name in CLI and API

**Dmitry Valter** <dvalter@protonmail.com>:

  | `40149 <https:////gerrit.fd.io/r/c/vpp/+/40149>`_ [VEc 13]: vppinfra: fix mask compare and compress OOB reads
  | `40150 <https:////gerrit.fd.io/r/c/vpp/+/40150>`_ [VeC 37]: vppinfra: fix test_vec invalid checks
  | `40123 <https:////gerrit.fd.io/r/c/vpp/+/40123>`_ [VeC 53]: fib: fix ip drop path crashes
  | `40122 <https:////gerrit.fd.io/r/c/vpp/+/40122>`_ [VeC 54]: vppapigen: fix enum format function
  | `40082 <https:////gerrit.fd.io/r/c/vpp/+/40082>`_ [VeC 60]: ip: mark ipX_header_t and ip4_address_t as packed
  | `40081 <https:////gerrit.fd.io/r/c/vpp/+/40081>`_ [VeC 66]: nat: fix det44 flaky test

**Emmanuel Scaria** <emmanuelscaria11@gmail.com>:

  | `40293 <https:////gerrit.fd.io/r/c/vpp/+/40293>`_ [VEc 4]: tcp: Start persist timer if snd_wnd is zero and no probing
  | `40129 <https:////gerrit.fd.io/r/c/vpp/+/40129>`_ [vec 51]: tcp: drop resets on tcp closed state Type: improvement Change-Id: If0318aa13a98ac4bdceca1b7f3b5d646b4b8d550 Signed-off-by: emmanuel <emmanuelscaria11@gmail.com>

**Filip Tehlar** <ftehlar@cisco.com>:

  | `40008 <https:////gerrit.fd.io/r/c/vpp/+/40008>`_ [vEc 23]: http: fix client receiving large data

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [veC 103]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VeC 92]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 92]: tests: fix issues found when enabling DMAC check

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 55]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 73]: interface: move set rss queues function

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `39937 <https:////gerrit.fd.io/r/c/vpp/+/39937>`_ [VeC 38]: vlib: improve core pinning
  | `40053 <https:////gerrit.fd.io/r/c/vpp/+/40053>`_ [VeC 60]: misc: move lawful-intercept to plugin

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 129]: ip: fix crash in ip4_neighbor_advertise

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 172]: sr: SRv6 Path Tracing source node behavior

**Kaj Niemi** <kajtzu@a51.org>:

  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VeC 125]: build: Enable building on AlmaLinux 9

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `40280 <https:////gerrit.fd.io/r/c/vpp/+/40280>`_ [vEC 5]: nat: add in2out-ip-fib-index config option

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 158]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VeC 82]: misc: tracedump specify cache size

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 76]: geneve: add support for layer 3

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 122]: vlib: allow overlapping cli subcommands

**Neale Ranns** <neale@graphiant.com>:

  | `40288 <https:////gerrit.fd.io/r/c/vpp/+/40288>`_ [vEC 7]: fib: Fix the make-before break load-balance construction    - ensure all DPOs are valid when used by workers. wait one loop for that as required.    - FIB UT to verify
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 96]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 163]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 163]: ip: Set the buffer error in ip6-input

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 54]: geneve: support custom options in decap

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VeC 89]: interface: check sw_if_index more thoroughly

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 129]: l2: fix crash while sending traffic out orphan BVI

**Vladislav Grishenko** <themiron@mail.ru>:

  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 131]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 138]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 138]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 138]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 138]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `40013 <https:////gerrit.fd.io/r/c/vpp/+/40013>`_ [veC 74]: nat: speed-up nat44-ed outside address distribution
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VeC 81]: vppapigen: recognize also _event as to_network
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 137]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 145]: ip-neighbor: add version 3 of neighbor event

**Wim de With** <wf@dewith.io>:

  | `40260 <https:////gerrit.fd.io/r/c/vpp/+/40260>`_ [vEC 9]: build: use GNUInstallDirs where possible

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 142]: interface dpdk avf: introducing setting RSS hash key feature

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 163]: af_xdp: optimizing send performance

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 151]: vrrp: dump vrrp vr peer

**kai zhang** <zhangkaiheb@126.com>:

  | `40241 <https:////gerrit.fd.io/r/c/vpp/+/40241>`_ [vEC 19]: dpdk: problem in parsing max-simd-bitwidth setting

**shaohui jin** <jinshaohui789@163.com>:

  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VeC 99]: vppinfra: fix memory overrun in mhash_set_mem
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 109]: ping:mark ipv6 packets as locally originated

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `39979 <https:////gerrit.fd.io/r/c/vpp/+/39979>`_ [VEc 30]: ipsec: move ah packet processing in the inline function ipsec_ah_packet_process

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [A 180]: dhcp: fix dhcp multiple client request

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
authors          56
maintainers      38
committers       1
abandoned        1
================ ===

