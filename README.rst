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
generated on Monday 2023-11-27, 02:03:35
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

  | `39997 <https:////gerrit.fd.io/r/c/vpp/+/39997>`_ [VECR 3]: bfd: fix buffer leak when cannot send periodic packets

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 15]: ethernet: check dmacs_bad in the fastpath case

avf: **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 4]: interface dpdk avf: introducing setting RSS hash key feature
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 15]: ethernet: check dmacs_bad in the fastpath case

build: **Damjan Marion** <damarion@cisco.com>
  | `39976 <https:////gerrit.fd.io/r/c/vpp/+/39976>`_ [VECr 5]: ipsec: Update host IPsec-mb lib

dev: **Damjan Marion** <damarion@cisco.com>
  | `39999 <https:////gerrit.fd.io/r/c/vpp/+/39999>`_ [VECr 1]: dev: initial set of APIs

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 3]: interface dpdk: refactor RSS queues feature
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 4]: interface dpdk avf: introducing setting RSS hash key feature
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 9]: dpdk: create and remove interface in runtime
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 15]: ethernet: check dmacs_bad in the fastpath case

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 3]: interface dpdk: refactor RSS queues feature
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 4]: interface dpdk avf: introducing setting RSS hash key feature
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 15]: ethernet: check dmacs_bad in the fastpath case

fib: **Neale Ranns** <neale@graphiant.com>
  | `40001 <https:////gerrit.fd.io/r/c/vpp/+/40001>`_ [VECr 2]: fib: fix fib_path_create() with drop targets

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `37610 <https:////gerrit.fd.io/r/c/vpp/+/37610>`_ [VECr 3]: http: unify client/server state machines

http: **Florin Coras** <fcoras@cisco.com>
  | `37610 <https:////gerrit.fd.io/r/c/vpp/+/37610>`_ [VECr 3]: http: unify client/server state machines

interface: **Dave Barach** <vpp@barachs.net>
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 3]: interface dpdk: refactor RSS queues feature
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 4]: interface dpdk avf: introducing setting RSS hash key feature
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 12]: interface: check sw_if_index more thoroughly
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 15]: ethernet: check dmacs_bad in the fastpath case

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `39943 <https:////gerrit.fd.io/r/c/vpp/+/39943>`_ [VECr 3]: l2: Resolve l2 Rewrite entry 'hit_count' always being 0 bug

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 15]: ethernet: check dmacs_bad in the fastpath case

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39999 <https:////gerrit.fd.io/r/c/vpp/+/39999>`_ [VECr 1]: dev: initial set of APIs
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 4]: interface dpdk avf: introducing setting RSS hash key feature
  | `39942 <https:////gerrit.fd.io/r/c/vpp/+/39942>`_ [VECr 5]: misc: tracedump specify cache size

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 15]: ethernet: check dmacs_bad in the fastpath case

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39761 <https:////gerrit.fd.io/r/c/vpp/+/39761>`_ [VECr 3]: tests: skip vcl tests with ASAN
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 15]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VECr 15]: tests: fix issues found when enabling DMAC check

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 4]: misc: patch to test CI infra changes

vppapigen: **Ole Troan** <otroan@employees.org>
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VECr 4]: vppapigen: recognize also _event as to_network

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `39862 <https:////gerrit.fd.io/r/c/vpp/+/39862>`_ [VECr 16]: vppinfra: change fchmod to umask for unix socket
  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VECr 22]: vppinfra: fix memory overrun in mhash_set_mem

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 81]: nat: nat44-ed get out2in workers failed for static mapping without port

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 121]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 121]: api trace: the api trace info about barrier is opposite

**Adrian Villin** <avillin@cisco.com>:

  | `39861 <https:////gerrit.fd.io/r/c/vpp/+/39861>`_ [vEC 2]: tests: Added tracedump plugin tests
  | `39900 <https:////gerrit.fd.io/r/c/vpp/+/39900>`_ [vEC 3]: tests: Added NSIM plugin tests

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 115]: linux-cp: Fix update on IPv4 routes

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [veC 72]: ena: add tx checksum offloads and tso support
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VeC 80]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 110]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VeC 32]: ip6: ECMP hash support for ipv6 fragments
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 32]: fib: log an error when destroying non-empty tables

**Damjan Marion** <dmarion@0xa5.net>:

  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 179]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 56]: libmemif: added tests
  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 81]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 179]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [vEC 26]: session: program rx events only if none are pending

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 52]: ip: fix crash in ip4_neighbor_advertise

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 95]: sr: SRv6 Path Tracing source node behavior

**Kaj Niemi** <kajtzu@a51.org>:

  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VeC 48]: build: Enable building on AlmaLinux 9

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 65]: linux-cp: Add VRF synchronization

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 122]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 81]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39871 <https:////gerrit.fd.io/r/c/vpp/+/39871>`_ [vEC 12]: tests: preload api files

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39778 <https:////gerrit.fd.io/r/c/vpp/+/39778>`_ [vEC 25]: devices: add support to check host interface offload capabilities
  | `35934 <https:////gerrit.fd.io/r/c/vpp/+/35934>`_ [vEC 25]: devices: add cli support to enable disable qdisc bypass
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 81]: geneve: add support for layer 3

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 45]: vlib: allow overlapping cli subcommands

**Naveen Joy** <najoy@cisco.com>:

  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VeC 61]: tests: memif ethernet type interface tests

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VEc 19]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 86]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 86]: ip: Set the buffer error in ip6-input

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 67]: geneve: support custom options in decap

**Pim van Pelt** <pim@ipng.nl>:

  | `39622 <https:////gerrit.fd.io/r/c/vpp/+/39622>`_ [VeC 41]: linux-cp: Fix looping netlink messages

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 123]: ipsec: introduce function esp_prepare_packet_for_enc

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 110]: ip: flow hash ignore tcp/udp ports when fragmented

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 52]: l2: fix crash while sending traffic out orphan BVI
  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 121]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 123]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 164]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Tianyu Li** <tianyu.li@arm.com>:

  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VeC 56]: libmemif: fix segfault and buffer overflow in examples

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 104]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vladislav Grishenko** <themiron@mail.ru>:

  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 54]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 61]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 61]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 61]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 61]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 60]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 68]: ip-neighbor: add version 3 of neighbor event

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 65]: interface dpdk avf: introducing setting RSS hash key feature

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 86]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 133]: ipsec: should use praddr_ instead of pladdr_

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 74]: vrrp: dump vrrp vr peer

**shaohui jin** <jinshaohui789@163.com>:

  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VeC 32]: ping:mark ipv6 packets as locally originated

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 103]: dhcp: fix dhcp multiple client request

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
authors          54
maintainers      17
committers       1
abandoned        0
================ ===

