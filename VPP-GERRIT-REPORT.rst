
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Friday 2026-09-04, 05:50:37
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

  | `46601 <https:////gerrit.fd.io/r/c/vpp/+/46601>`_ [VECR 3]: hs-test: enable pcap via make test option
  | `46619 <https:////gerrit.fd.io/r/c/vpp/+/46619>`_ [VECR 6]: hs-test: dump backtrace of all threads
  | `46598 <https:////gerrit.fd.io/r/c/vpp/+/46598>`_ [VECR 6]: hs-test: test-wipe make target

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

abf: **Neale Ranns** <neale@graphiant.com>
  | `46339 <https:////gerrit.fd.io/r/c/vpp/+/46339>`_ [VECr 22]: abf: reject attachment to a non-existent policy instead of asserting

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `46481 <https:////gerrit.fd.io/r/c/vpp/+/46481>`_ [VECr 2]: acl: add callback hooks for list add/del

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `46539 <https:////gerrit.fd.io/r/c/vpp/+/46539>`_ [VECr 0]: af_xdp: add optional socket busy polling

build: **Damjan Marion** <damarion@cisco.com>
  | `46392 <https:////gerrit.fd.io/r/c/vpp/+/46392>`_ [VECr 6]: octeon: update octeon roc version

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `46471 <https:////gerrit.fd.io/r/c/vpp/+/46471>`_ [VECr 1]: cnat: improve flow statistics and error coverage

dev: **Damjan Marion** <damarion@cisco.com>
  | `46480 <https:////gerrit.fd.io/r/c/vpp/+/46480>`_ [VECr 1]: dev: relax queue-per-thread rx placement strategy
  | `46393 <https:////gerrit.fd.io/r/c/vpp/+/46393>`_ [VECr 6]: dev: add port attribute for speed capability
  | `46282 <https:////gerrit.fd.io/r/c/vpp/+/46282>`_ [VECr 12]: dev: advertise TX UDP GSO

dispatch-trace: **Dave Barach** <vpp@barachs.net>
  | `46469 <https:////gerrit.fd.io/r/c/vpp/+/46469>`_ [VECr 4]: dispatch-trace: fix SIGSEGV/SIGABRT on multi-worker handoff

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 0]: rdma: add mlx5 DV TSO support for raw packet tx
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 1]: misc: patch to test CI infra
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 1]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [VECr 2]: misc: surs patch to test CI infra
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 11]: iavf: add setup documentation
  | `46529 <https:////gerrit.fd.io/r/c/vpp/+/46529>`_ [VECr 14]: docs: Get the VPP Source
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VECr 15]: lb: add NAT6_NOPORT encap type

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 1]: dpdk: log MFIB MAC replay tolerance at debug level
  | `45699 <https:////gerrit.fd.io/r/c/vpp/+/45699>`_ [VECr 27]: dpdk: buffer bug fixes

fib: **Neale Ranns** <neale@graphiant.com>
  | `46338 <https:////gerrit.fd.io/r/c/vpp/+/46338>`_ [VECr 22]: fib: tolerate a NULL rewrite in vnet_rewrite_for_sw_interface

flow: **Damjan Marion** <damarion@cisco.com>
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 7]: flow: add flow template and async range infrastructure

gha: **Dave Wallace** <dwallacelf@gmail.com>
  | `46530 <https:////gerrit.fd.io/r/c/vpp/+/46530>`_ [VECr 14]: gha: skip build/test verify jobs for docs-only changes

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `46717 <https:////gerrit.fd.io/r/c/vpp/+/46717>`_ [VECr 0]: hsa: coverity fixes CIDs 563417, 563388
  | `46675 <https:////gerrit.fd.io/r/c/vpp/+/46675>`_ [VECr 2]: hs-test: suppress mem-leak report noise
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 10]: vperf: drop residual echo/vcl_test terminology

http: **Florin Coras** <fcoras@cisco.com>
  | `46710 <https:////gerrit.fd.io/r/c/vpp/+/46710>`_ [VECr 0]: http: add more counters
  | `46673 <https:////gerrit.fd.io/r/c/vpp/+/46673>`_ [VECr 1]: http: fix multiple ASAN memory-safety bugs

iavf: **Damjan Marion** <damarion@cisco.com>
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 11]: iavf: add setup documentation
  | `46283 <https:////gerrit.fd.io/r/c/vpp/+/46283>`_ [VECr 12]: iavf: add UDP segmentation offload support
  | `46271 <https:////gerrit.fd.io/r/c/vpp/+/46271>`_ [VECr 12]: iavf: fix iavf_tx_fill_ctx_desc ph buf seg fault
  | `46261 <https:////gerrit.fd.io/r/c/vpp/+/46261>`_ [VECr 12]: iavf: fix rx queue max_pkt_size value set on init

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 7]: ipsec: IPTFS (RFC 9347) support

interface: **Dave Barach** <vpp@barachs.net>
  | `46651 <https:////gerrit.fd.io/r/c/vpp/+/46651>`_ [VECr 0]: vnet: keep deleted interface node names unique
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [VECr 7]: flow: add flow template and async range infrastructure

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VECr 1]: ip: fix adjacent packet overwrite with ip frags
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 7]: ipsec: IPTFS (RFC 9347) support
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 30]: ip: fix punt socket rx when multiple FDs are ready

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 7]: ipsec: IPTFS (RFC 9347) support

kube-test: **Florin Coras** <fcoras@cisco.com>
  | `46593 <https:////gerrit.fd.io/r/c/vpp/+/46593>`_ [VECr 2]: tests: bypass http/https proxy in test curl invocations
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 10]: vperf: drop residual echo/vcl_test terminology

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `46526 <https:////gerrit.fd.io/r/c/vpp/+/46526>`_ [VECr 15]: lb: fix NAT66 UDP/IPv6 checksum zero-fold
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VECr 15]: lb: add NAT6_NOPORT encap type

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [VECr 1]: linux-cp: tolerate missing neighbor on delete

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 1]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 7]: ipsec: IPTFS (RFC 9347) support
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 10]: vperf: drop residual echo/vcl_test terminology
  | `46442 <https:////gerrit.fd.io/r/c/vpp/+/46442>`_ [VECr 21]: vnet: install missing vnet headers

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `46577 <https:////gerrit.fd.io/r/c/vpp/+/46577>`_ [VECr 2]: octeon: fix port start return value
  | `46425 <https:////gerrit.fd.io/r/c/vpp/+/46425>`_ [VECr 6]: octeon: add support to set link-speed
  | `46576 <https:////gerrit.fd.io/r/c/vpp/+/46576>`_ [VECr 8]: octeon: fix drain queue

papi: **Ole Troan** <otroan@employees.org>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46555 <https:////gerrit.fd.io/r/c/vpp/+/46555>`_ [VECr 7]: papi: use public ipaddress .version (Python 3.14/Ubuntu 26.04)

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46641 <https:////gerrit.fd.io/r/c/vpp/+/46641>`_ [VECr 1]: quic: fix ASAN error while reading cert/key data
  | `46315 <https:////gerrit.fd.io/r/c/vpp/+/46315>`_ [VECr 10]: quic: quic_quicly add uso support

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `46465 <https:////gerrit.fd.io/r/c/vpp/+/46465>`_ [VECr 0]: rdma: add mlx5 enhanced MPW with optional inline
  | `46155 <https:////gerrit.fd.io/r/c/vpp/+/46155>`_ [VECr 0]: rdma: fix verbs port selection
  | `46667 <https:////gerrit.fd.io/r/c/vpp/+/46667>`_ [VECr 0]: rdma: stop mlx5 DV queues after completion error
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 0]: rdma: add mlx5 DV TSO support for raw packet tx
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 1]: rdma: steer PPPoE discovery and session flows

session: **Florin Coras** <fcoras@cisco.com>
  | `46642 <https:////gerrit.fd.io/r/c/vpp/+/46642>`_ [VECr 1]: session: fix ASAN stack overflow and use-after-realloc
  | `46379 <https:////gerrit.fd.io/r/c/vpp/+/46379>`_ [VECr 6]: session: add half_close support for cut-through transport
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 10]: udp: add segmentation offload support
  | `46473 <https:////gerrit.fd.io/r/c/vpp/+/46473>`_ [VECr 20]: session: revalidate ct listener during accept
  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [VECr 30]: session: check event collector lookups

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `46362 <https:////gerrit.fd.io/r/c/vpp/+/46362>`_ [VECr 2]: sfdp: add api sfdp_kill_session_batch

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service

srtp: **Florin Coras** <fcoras@cisco.com>
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 10]: vperf: drop residual echo/vcl_test terminology

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46554 <https:////gerrit.fd.io/r/c/vpp/+/46554>`_ [VECr 0]: tests: fix multiprocessing Python 3.14 failures on Ubuntu 26.04
  | `46539 <https:////gerrit.fd.io/r/c/vpp/+/46539>`_ [VECr 0]: af_xdp: add optional socket busy polling
  | `46651 <https:////gerrit.fd.io/r/c/vpp/+/46651>`_ [VECr 0]: vnet: keep deleted interface node names unique
  | `46719 <https:////gerrit.fd.io/r/c/vpp/+/46719>`_ [VECr 0]: tests: avoid iperf preexec deadlocks
  | `46720 <https:////gerrit.fd.io/r/c/vpp/+/46720>`_ [VECr 0]: tests: make qemu network lock recoverable
  | `46636 <https:////gerrit.fd.io/r/c/vpp/+/46636>`_ [VECr 0]: tests: avoid repeated pg barriers awaiting capture
  | `46579 <https:////gerrit.fd.io/r/c/vpp/+/46579>`_ [VECr 0]: misc: patch to test maketest action timeout
  | `46640 <https:////gerrit.fd.io/r/c/vpp/+/46640>`_ [VECr 0]: tests: tolerate delayed BFD observations
  | `46471 <https:////gerrit.fd.io/r/c/vpp/+/46471>`_ [VECr 1]: cnat: improve flow statistics and error coverage
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 1]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46593 <https:////gerrit.fd.io/r/c/vpp/+/46593>`_ [VECr 2]: tests: bypass http/https proxy in test curl invocations
  | `46657 <https:////gerrit.fd.io/r/c/vpp/+/46657>`_ [VECr 2]: nat: tolerate unchanged translated ports
  | `46362 <https:////gerrit.fd.io/r/c/vpp/+/46362>`_ [VECr 2]: sfdp: add api sfdp_kill_session_batch
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 8]: vlib: add per-thread index pool cache
  | `46166 <https:////gerrit.fd.io/r/c/vpp/+/46166>`_ [VECr 10]: vperf: drop residual echo/vcl_test terminology
  | `46541 <https:////gerrit.fd.io/r/c/vpp/+/46541>`_ [VECr 11]: tests: preserve LD_PRELOAD across stdbuf on uutils (Rust)
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VECr 15]: lb: add NAT6_NOPORT encap type
  | `46338 <https:////gerrit.fd.io/r/c/vpp/+/46338>`_ [VECr 22]: fib: tolerate a NULL rewrite in vnet_rewrite_for_sw_interface
  | `46339 <https:////gerrit.fd.io/r/c/vpp/+/46339>`_ [VECr 22]: abf: reject attachment to a non-existent policy instead of asserting

udp: **Florin Coras** <fcoras@cisco.com>
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 10]: udp: add segmentation offload support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `46718 <https:////gerrit.fd.io/r/c/vpp/+/46718>`_ [VECr 0]: unittest: tcp_test coverity fix CID 563389
  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VECr 7]: ipsec: IPTFS (RFC 9347) support
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 8]: vlib: add per-thread index pool cache

vcl: **Florin Coras** <fcoras@cisco.com>
  | `46590 <https:////gerrit.fd.io/r/c/vpp/+/46590>`_ [VECr 0]: vcl: fix asan bug found in hs-test
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 1]: misc: patch to test CI infra
  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [VECr 2]: misc: surs patch to test CI infra
  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VECr 13]: vcl: LDP default to regular option

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 8]: vlib: add per-thread index pool cache
  | `46546 <https:////gerrit.fd.io/r/c/vpp/+/46546>`_ [VECr 11]: vlib: re-base the timing wheel when arming an empty wheel
  | `46434 <https:////gerrit.fd.io/r/c/vpp/+/46434>`_ [VECr 27]: vlib: fix log2 histogram overflow bin writing past the bin vector

vperf: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `46717 <https:////gerrit.fd.io/r/c/vpp/+/46717>`_ [VECr 0]: hsa: coverity fixes CIDs 563417, 563388

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 1]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 8]: sfdp: add sfdp-session-stats service

vppapigen: **Ole Troan** <otroan@employees.org>
  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VECr 1]: vppapigen: fix inconsistency in paths JSON

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `46372 <https:////gerrit.fd.io/r/c/vpp/+/46372>`_ [VECr 29]: vppinfra: do not apply VEC512 tricks for ip6

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [Vec 80]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 87]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 87]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vEc 3]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 104]: snort: don't store snort metadata in buffer

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vec 49]: crypto: openssl - check ctx alloc/init in key-add
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 127]: map: enhance map plugin to support per-vrf rules

**Anton Blazhko** <ablazhko@cisco.com>:

  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [Vec 50]: devices: Convert PIPE to plugin

**Aritra Basu** <aritrbas@cisco.com>:

  | `46661 <https:////gerrit.fd.io/r/c/vpp/+/46661>`_ [VEc 0]: vperf: fix ASAN buffer over-read and memory leaks
  | `46265 <https:////gerrit.fd.io/r/c/vpp/+/46265>`_ [VeC 35]: vcl: add vls_unregister_vcl_worker for explicit worker teardown
  | `46249 <https:////gerrit.fd.io/r/c/vpp/+/46249>`_ [VeC 52]: kube-test: inherit pod MTU for memif test tap
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [Vec 58]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VeC 65]: tcp: add TCP fast open support (RFC 7413)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [veC 69]: kube-test: retry Job finalizer cleanup conflicts
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 83]: interface: enable IPv6 link state on unnumbered interfaces
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 83]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 167]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 169]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 169]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 169]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 169]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 175]: ip6-nd: fix unicast NA handling in ND proxy

**Benoît Ganne** <bganne@cisco.com>:

  | `46368 <https:////gerrit.fd.io/r/c/vpp/+/46368>`_ [VeC 37]: vppinfra: make vec_foreach_pointer empty-safe
  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VeC 73]: vppapigen: fix vppapigen depfile without imports
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VeC 73]: cnat: wait for cnat scanner session cleanup

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 90]: ikev2: add Curve25519 and Curve448 DH groups

**Dave Wallace** <dwallacelf@gmail.com>:

  | `46075 <https:////gerrit.fd.io/r/c/vpp/+/46075>`_ [vEC 1]: docs: update tsc vulnerability management process

**Dennis Lanov** <dennis.lanov@gmail.com>:

  | `46270 <https:////gerrit.fd.io/r/c/vpp/+/46270>`_ [VeC 50]: acl: correct interface command help

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 171]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 171]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**Florin Coras** <florin.coras@gmail.com>:

  | `46687 <https:////gerrit.fd.io/r/c/vpp/+/46687>`_ [vEC 2]: vppinfra: avoid duplicate rbtree custom comparison

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VeC 80]: crypto: add op tracing capability
  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 120]: dpdk: tracing improvements

**GregMiller** <greg@gregmiller.co.za>:

  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VeC 72]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VeC 72]: pppoe: add combined subscriber session provisioning API

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `46588 <https:////gerrit.fd.io/r/c/vpp/+/46588>`_ [vEC 3]: sfdp_services: various sfdp nat improvements
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VeC 64]: sfdp: modify tenant_index type from u16 to u32
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VeC 71]: flow: add parameter to pre-allocate global pool
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [veC 71]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VeC 71]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [veC 71]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [Vec 72]: sfdp: add verdict-testbench service
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VeC 72]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VeC 72]: flow: add flow aging support
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 84]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 84]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 87]: tracepath: minor refactoring to code
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 108]: sfdp: fix specification of scope_index

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VeC 73]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [Vec 69]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [Vec 73]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 161]: tests: reduce sleep interval in ip-neighbor age test

**Janik** <janik.haag@imc.com>:

  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [Vec 44]: build: fix make install-deps for fedora targets
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VeC 73]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VeC 73]: vcl: add regression test for ignorable flags
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VeC 73]: sasc: fix gcc uninitialized warning

**Jerome Tollet** <jtollet@cisco.com>:

  | `46609 <https:////gerrit.fd.io/r/c/vpp/+/46609>`_ [vEC 0]: rdma: enforce mlx5 DV DMA ordering
  | `46634 <https:////gerrit.fd.io/r/c/vpp/+/46634>`_ [vEC 0]: tests: preserve timeout diagnostics across retries
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [vEC 1]: vnet: use hidden visibility with explicit exports
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VeC 36]: iavf: fix native TSO datapath
  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VeC 114]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VeC 114]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VeC 114]: tcp: allow selective GRO enablement
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 128]: virtio: add native plugin L2 xconnect test with QEMU

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 85]: ip bonding hash: inner-aware flow hash (opt-in)

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 153]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 153]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Keith Spinney** <kspinney@cisco.com>:

  | `46525 <https:////gerrit.fd.io/r/c/vpp/+/46525>`_ [VEc 9]: fib: barrier-protect fib_path_list_destroy()

**Klement Sekera** <ksekera@netgate.com>:

  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VeC 51]: build: include GNUInstallDirs in VPPConfig
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VeC 51]: api: add build-time python stub generation via vppapigen
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 134]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 84]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 84]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <mfabianlf@pm.me>:

  | `46079 <https:////gerrit.fd.io/r/c/vpp/+/46079>`_ [veC 69]: hs-test: temporarily disable core file removal

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vec 62]: dpdk: support async flow offload
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [veC 85]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 91]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [vec 91]: flow: add per-thread flow pool cache for multi-worker safety
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 91]: dpdk: multi-thread async flow offload with per-worker caches
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 164]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 164]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 170]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 170]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 170]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 170]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [veC 104]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VEc 17]: ipip: fix support for ipip6o6 from linux tunnel
  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 149]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 169]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 175]: sfdp: add blacklist/whitelist to snort service

**Monendra Singh Kushwaha** <kmonendra@marvell.com>:

  | `46575 <https:////gerrit.fd.io/r/c/vpp/+/46575>`_ [vEC 4]: octeon: fix flow parsing in octeon driver

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 148]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 148]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 156]: ip6: fix show ip6-ll cli if selector

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 91]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `46511 <https:////gerrit.fd.io/r/c/vpp/+/46511>`_ [vEC 0]: stats: add directory command to vpp_get_stats
  | `46380 <https:////gerrit.fd.io/r/c/vpp/+/46380>`_ [Vec 34]: vppapigen: fix unaligned access to packed messages
  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 141]: papi: improve performance on set_errors

**Pim van Pelt** <pim@ipng.nl>:

  | `46038 <https:////gerrit.fd.io/r/c/vpp/+/46038>`_ [Vec 78]: ip6-nd: fix crash in link-local target NS
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 148]: lb: Add punt feature to per-port VIPs

**Poornima Kandhade** <poornika@cisco.com>:

  | `46424 <https:////gerrit.fd.io/r/c/vpp/+/46424>`_ [vEC 6]: sfdp: add lifecycle records to session stats ring

**Qi Zhang** <zzqqqqwq77@gmail.com>:

  | `46458 <https:////gerrit.fd.io/r/c/vpp/+/46458>`_ [vEC 4]: vlib: detect freed buffer‑chain on node dispatch for double‑free debug
  | `46643 <https:////gerrit.fd.io/r/c/vpp/+/46643>`_ [vEC 4]: vnet: fix double-free in bcast fragment reassembly

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 99]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 111]: octeon: add PFC support

**Robert Shearman** <robertshearman@gmail.com>:

  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [vEC 1]: vlib: ASAN-poison unallocated buffers
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [vEC 30]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [vEC 30]: ip: fix adjacent packet overwrite with ip6 frags
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [vec 39]: misc: fix potential OOB read during flow hash calculations

**Samuel Benko** <sbenko@cisco.com>:

  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VeC 71]: tls: propagate verify config for dtls

**Sergiy Bachynskyy** <sbachyns@cisco.com>:

  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VeC 57]: ipfix: move to a plugin

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46355 <https:////gerrit.fd.io/r/c/vpp/+/46355>`_ [VeC 37]: ip: fix fragmentation with negative buffer offset
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [VeC 37]: session: validate app for async connect RPC
  | `46352 <https:////gerrit.fd.io/r/c/vpp/+/46352>`_ [VeC 39]: vppinfra: serialize VM map page size lookup
  | `46341 <https:////gerrit.fd.io/r/c/vpp/+/46341>`_ [VeC 41]: hsa: make TLS client CLI MP-safe
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VeC 43]: tcp: handle retransmitted SYN-ACK in TIME-WAIT

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `46370 <https:////gerrit.fd.io/r/c/vpp/+/46370>`_ [VeC 35]: vlib: fix cli mem leak in line mode
  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VeC 37]: fib: dump by src not only contributing routes

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [Vec 50]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [Vec 51]: bfd: Extract to plugin

**Vladimir Lavor** <vlavor@cisco.com>:

  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VeC 49]: vlib: expose error severity in stats segment

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 108]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 156]: vppinfra: collect heap stats in constant time

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 97]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 141]: empty change for GHA(CSIT) testing

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [Vec 70]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 99]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 99]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 100]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 101]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 106]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [Vec 62]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [Vec 43]: ip6-nd: support RDNSS option in IPv6 RA
  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [Vec 43]: ip6-nd: update secondary RA prefixes for subnets

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 115]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 156]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 156]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 157]: build rpm-packaging: make vpp rpm package for kylinV11

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 129]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [veC 77]: cnat: add scope_id to session key

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 168]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 156]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 156]: lb: fix API byte order and IPv4 prefix length handling

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 125]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 112]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 114]: tls: fix picotls partial record handling
  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 115]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 121]: session: make transport to use application's segment manager

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
authors          148
maintainers      70
committers       3
abandoned        0
================ ===

