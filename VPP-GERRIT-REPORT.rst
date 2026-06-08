
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Monday 2026-06-08, 06:05:59
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

  | `45968 <https:////gerrit.fd.io/r/c/vpp/+/45968>`_ [VECR 0]: tests: allow disabling 'clear trace' in pg_start
  | `45959 <https:////gerrit.fd.io/r/c/vpp/+/45959>`_ [VECR 4]: lldp: fix TLV validation
  | `45891 <https:////gerrit.fd.io/r/c/vpp/+/45891>`_ [VECR 10]: quic: increase default fifo size to 512k

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

bonding: **Steven Luong** <sluong@cisco.com>
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 12]: ip bonding hash: inner-aware flow hash (opt-in)

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 4]: vlib: ASAN-poison unallocated buffers

build: **Damjan Marion** <damarion@cisco.com>
  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [VECr 0]: vppinfra: add loongarch64 architecture support
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VECr 0]: build: include GNUInstallDirs in VPPConfig
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 3]: dpdk: install default jump-to-group-1 rule for mlx5

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [VECr 2]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get
  | `45882 <https:////gerrit.fd.io/r/c/vpp/+/45882>`_ [VECr 3]: cnat: guard snat policy APIs against NULL policy entry
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 18]: cnat: add scope_id to session key

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 2]: misc: patch to test CI infra
  | `45916 <https:////gerrit.fd.io/r/c/vpp/+/45916>`_ [VECr 2]: sfdp_services: change fsol-non-syn behavior in l4-lifecycle
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 12]: ip bonding hash: inner-aware flow hash (opt-in)
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 17]: sfdp: add sfdp-session-stats service
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 18]: cnat: add scope_id to session key
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 25]: rdma: add mlx5 TSO support for raw packet tx
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VECr 26]: tcp: allow selective GRO enablement

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 2]: flow: restructure vnet_flow_t for cache-line optimization
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VECr 3]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [VECr 5]: dpdk: add support for represented port action
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VECr 25]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VECr 25]: dpdk: add support for VNET_FLOW_ACTION_AGE action

flow: **Damjan Marion** <damarion@cisco.com>
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 2]: flow: restructure vnet_flow_t for cache-line optimization
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VECr 4]: flow: add parameter to pre-allocate global pool
  | `45908 <https:////gerrit.fd.io/r/c/vpp/+/45908>`_ [VECr 5]: flow: add max parameter in 'show flow entry' CLI
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VECr 5]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VECr 25]: flow: add flow aging support
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [VECr 25]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 2]: flow: restructure vnet_flow_t for cache-line optimization

hash: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 12]: ip bonding hash: inner-aware flow hash (opt-in)

hs-test: **Florin Coras** <fcoras@cisco.com>, **Matus Fabian** <matfabia@cisco.com>
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 13]: vlib: fix process state format output wrapped by extra quotes
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 24]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VECr 26]: tls: fix picotls partial record handling

http: **Florin Coras** <fcoras@cisco.com>
  | `45999 <https:////gerrit.fd.io/r/c/vpp/+/45999>`_ [VECr 3]: http: h2 limit total size of fragmented headers

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 16]: iavf: fix native TSO datapath

interface: **Dave Barach** <vpp@barachs.net>
  | `45850 <https:////gerrit.fd.io/r/c/vpp/+/45850>`_ [VECr 19]: interface: no-mfib table bind and create fixes

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `46000 <https:////gerrit.fd.io/r/c/vpp/+/46000>`_ [VECr 2]: ip6: fix potential small OOB read in extension header walk
  | `45913 <https:////gerrit.fd.io/r/c/vpp/+/45913>`_ [VECr 3]: ip: fix data race of fragment ID
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VECr 4]: ip: fix adjacent packet overwrite with ip frags
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VECr 4]: ip: fix adjacent packet overwrite with ip6 frags
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 12]: ip bonding hash: inner-aware flow hash (opt-in)
  | `45850 <https:////gerrit.fd.io/r/c/vpp/+/45850>`_ [VECr 19]: interface: no-mfib table bind and create fixes
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 23]: ip: svr add bit indicating fragmentation to vnet_buffer

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `45997 <https:////gerrit.fd.io/r/c/vpp/+/45997>`_ [VECr 2]: ipsec: ipsec_sa_add_and_lock(): fix and consolidate fail path

kube-test: **Florin Coras** <fcoras@cisco.com>
  | `45951 <https:////gerrit.fd.io/r/c/vpp/+/45951>`_ [VECr 5]: kube-test: bound kubectl rollout status to avoid 30m hangs

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `45478 <https:////gerrit.fd.io/r/c/vpp/+/45478>`_ [VECr 23]: ip: svr add bit indicating fragmentation to vnet_buffer

octeon: **Monendra Singh Kushwaha** <kmonendra@marvell.com>, **Damjan Marion** <damarion@cisco.com>
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 2]: flow: restructure vnet_flow_t for cache-line optimization
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VECr 23]: octeon: add PFC support

pvti: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `45956 <https:////gerrit.fd.io/r/c/vpp/+/45956>`_ [VECr 4]: pvti: fix adjacent packet overwrite with very big packets

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `45998 <https:////gerrit.fd.io/r/c/vpp/+/45998>`_ [VECr 3]: quic: connection timer init refactoring
  | `45975 <https:////gerrit.fd.io/r/c/vpp/+/45975>`_ [VECr 3]: quic: connection counters improvement
  | `45996 <https:////gerrit.fd.io/r/c/vpp/+/45996>`_ [VECr 3]: quic: transport param set disable_active_migration
  | `45946 <https:////gerrit.fd.io/r/c/vpp/+/45946>`_ [VECr 3]: quic: quic_quicly cid encryptor improvement
  | `45966 <https:////gerrit.fd.io/r/c/vpp/+/45966>`_ [VECr 4]: session: rename quic data in crypto ctx

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 25]: rdma: add mlx5 TSO support for raw packet tx

session: **Florin Coras** <fcoras@cisco.com>
  | `46015 <https:////gerrit.fd.io/r/c/vpp/+/46015>`_ [VECr 0]: session: defer ct segment cleanup for shared fifos
  | `45966 <https:////gerrit.fd.io/r/c/vpp/+/45966>`_ [VECr 4]: session: rename quic data in crypto ctx

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VECr 20]: sfdp: fix specification of scope_index

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `45916 <https:////gerrit.fd.io/r/c/vpp/+/45916>`_ [VECr 2]: sfdp_services: change fsol-non-syn behavior in l4-lifecycle
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 17]: sfdp: add sfdp-session-stats service

snort: **Damjan Marion** <damarion@cisco.com>
  | `45915 <https:////gerrit.fd.io/r/c/vpp/+/45915>`_ [VECr 9]: snort: fix wrong variable reference
  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VECr 16]: snort: don't store snort metadata in buffer

svm: **Dave Barach** <vpp@barachs.net>
  | `46015 <https:////gerrit.fd.io/r/c/vpp/+/46015>`_ [VECr 0]: session: defer ct segment cleanup for shared fifos

tcp: **Florin Coras** <fcoras@cisco.com>
  | `45775 <https:////gerrit.fd.io/r/c/vpp/+/45775>`_ [VECr 26]: tcp: fix pure ACK incorrectly chained as GRO candidate
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VECr 26]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VECr 26]: tcp: allow selective GRO enablement

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46014 <https:////gerrit.fd.io/r/c/vpp/+/46014>`_ [VECr 0]: tests: add extra_vpp_heap_config knob for main-heap-size
  | `46001 <https:////gerrit.fd.io/r/c/vpp/+/46001>`_ [VECr 2]: tests: halt parallel suites gracefully on FAILFAST
  | `46000 <https:////gerrit.fd.io/r/c/vpp/+/46000>`_ [VECr 2]: ip6: fix potential small OOB read in extension header walk
  | `45916 <https:////gerrit.fd.io/r/c/vpp/+/45916>`_ [VECr 2]: sfdp_services: change fsol-non-syn behavior in l4-lifecycle
  | `45913 <https:////gerrit.fd.io/r/c/vpp/+/45913>`_ [VECr 3]: ip: fix data race of fragment ID
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 4]: vlib: ASAN-poison unallocated buffers
  | `45937 <https:////gerrit.fd.io/r/c/vpp/+/45937>`_ [VECr 6]: tracepath: add api to dump trace paths
  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [VECr 12]: ip bonding hash: inner-aware flow hash (opt-in)
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 17]: sfdp: add sfdp-session-stats service
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [VECr 18]: cnat: add scope_id to session key
  | `45850 <https:////gerrit.fd.io/r/c/vpp/+/45850>`_ [VECr 19]: interface: no-mfib table bind and create fixes
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VECr 20]: sfdp: fix specification of scope_index
  | `45837 <https:////gerrit.fd.io/r/c/vpp/+/45837>`_ [VECr 24]: tests: add suffix to failed_test file
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 24]: tls: add ALPN negotiation support

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VECr 24]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VECr 26]: tls: fix picotls partial record handling

tracepath: **Hadi Rayan Al-Sandid** <halsandi@cisco.com>
  | `45937 <https:////gerrit.fd.io/r/c/vpp/+/45937>`_ [VECr 6]: tracepath: add api to dump trace paths

vcl: **Florin Coras** <fcoras@cisco.com>
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 2]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46005 <https:////gerrit.fd.io/r/c/vpp/+/46005>`_ [VECr 2]: vlib: add per-thread pool cache primitive
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VECr 13]: vlib: fix process state format output wrapped by extra quotes

vpp: **Dave Barach** <vpp@barachs.net>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 17]: sfdp: add sfdp-session-stats service

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [VECr 0]: vppinfra: add loongarch64 architecture support
  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VECr 11]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `45248 <https:////gerrit.fd.io/r/c/vpp/+/45248>`_ [VECr 2]: flow: restructure vnet_flow_t for cache-line optimization

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [VeC 37]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 103]: cnat: fix show cnat translation for specific translation id
  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 103]: cnat: fix show cnat client showing invalid for client id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vec 68]: vhost: fix rxvq interrupts triggered because of race

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `41210 <https:////gerrit.fd.io/r/c/vpp/+/41210>`_ [veC 137]: build: disable the "new" way of handling API dependencies which relies on a broken CMake feature

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 39]: map: enhance map plugin to support per-vrf rules

**Anna Neiman** <anna.neiman@insidepacket.com>:

  | `43046 <https:////gerrit.fd.io/r/c/vpp/+/43046>`_ [VeC 165]: feature: Call dvr_dpo_unlock in case delete SW interface - in order enable feature ip4-dvr-reinject on the following addition interface ;add arch index in show features

**Aritra Basu** <aritrbas@cisco.com>:

  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [vEc 2]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 47]: vlib: fix trace flag loss when multiple pending frames share next frame
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 51]: interface: enable IPv6 link state on unnumbered interfaces
  | `45012 <https:////gerrit.fd.io/r/c/vpp/+/45012>`_ [VeC 79]: ip-neighbor: suppress off-link adj-fib on addressed interfaces
  | `45268 <https:////gerrit.fd.io/r/c/vpp/+/45268>`_ [VeC 81]: ip6-nd: enforce on-link source validation for RS neighbor learning
  | `45073 <https:////gerrit.fd.io/r/c/vpp/+/45073>`_ [VeC 81]: fib: honor unnumbered RX interface in MFIB RPF check
  | `45074 <https:////gerrit.fd.io/r/c/vpp/+/45074>`_ [VeC 81]: ip6-nd: enforce on-link source validation for ND learning
  | `45260 <https:////gerrit.fd.io/r/c/vpp/+/45260>`_ [VeC 81]: ip6-nd: add per-interface control for inbound RA acceptance
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VeC 87]: ip6-nd: fix unicast NA handling in ND proxy

**Bartlomiej Leszak** <bartlomiej.leszak@gmail.com>:

  | `42978 <https:////gerrit.fd.io/r/c/vpp/+/42978>`_ [VeC 165]: pnat: do not disable pnat on rule deletion

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [vEC 2]: ikev2: add Curve25519 and Curve448 DH groups

**FDio GitHub Actions** <releng+fdio-github@linuxfoundation.org>:

  | `45227 <https:////gerrit.fd.io/r/c/vpp/+/45227>`_ [veC 83]: build(deps): bump step-security/harden-runner from 2.13.2 to 2.16.0
  | `45225 <https:////gerrit.fd.io/r/c/vpp/+/45225>`_ [veC 83]: build(deps): bump lfreleng-actions/github2gerrit-action from 1.0.5 to 1.0.8

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `45965 <https:////gerrit.fd.io/r/c/vpp/+/45965>`_ [VEc 0]: tests: pg: add maxframe parameter
  | `45684 <https:////gerrit.fd.io/r/c/vpp/+/45684>`_ [VeC 31]: buffers: return values; improve debug
  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 32]: dpdk: tracing improvements
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [VeC 33]: crypto: add op tracing capability

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [VEc 2]: sfdp: add verdict-testbench service
  | `45564 <https:////gerrit.fd.io/r/c/vpp/+/45564>`_ [Vec 40]: sfdp: add api enum for timeouts
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [Vec 104]: sfdp: modify tenant_index type from u16 to u32
  | `44474 <https:////gerrit.fd.io/r/c/vpp/+/44474>`_ [Vec 151]: sasc: fix tenant_index overlap in sasc_buffer

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `45696 <https:////gerrit.fd.io/r/c/vpp/+/45696>`_ [VEc 3]: cnat: make cnat pluggable
  | `45707 <https:////gerrit.fd.io/r/c/vpp/+/45707>`_ [VeC 33]: npol: wire npol into the cnat slow-path hook mechanism

**Ivan Ivanets** <iivanets@cisco.com>:

  | `42150 <https:////gerrit.fd.io/r/c/vpp/+/42150>`_ [VeC 73]: tests: reduce sleep interval in ip-neighbor age test
  | `44827 <https:////gerrit.fd.io/r/c/vpp/+/44827>`_ [VeC 102]: crypto: unify per-thread key_data allocation

**Jerome Labidurie** <jerome.labidurie@orange.com>:

  | `44849 <https:////gerrit.fd.io/r/c/vpp/+/44849>`_ [VeC 121]: policer: api to unaply policer from any interface
  | `44844 <https:////gerrit.fd.io/r/c/vpp/+/44844>`_ [VeC 121]: policer: prevent policer to be applied twice
  | `44843 <https:////gerrit.fd.io/r/c/vpp/+/44843>`_ [VeC 121]: policer: fix crash when unapplying a policer
  | `44693 <https:////gerrit.fd.io/r/c/vpp/+/44693>`_ [VeC 121]: policer: obtain policers applied to an interface

**Jerome Tollet** <jtollet@cisco.com>:

  | `46010 <https:////gerrit.fd.io/r/c/vpp/+/46010>`_ [vEC 0]: rdma: fix striding RQ multiseg buffer length
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 40]: virtio: add native plugin L2 xconnect test with QEMU
  | `45033 <https:////gerrit.fd.io/r/c/vpp/+/45033>`_ [VeC 41]: af_xdp: add support for multi-buffer

**Jiajun Liang** <3138947285@qq.com>:

  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [vEC 1]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `45677 <https:////gerrit.fd.io/r/c/vpp/+/45677>`_ [vEC 1]: linux-cp: guard PPPOX interface type and tolerate missing neighbor
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [vEC 1]: dpdk: log MFIB MAC replay tolerance at debug level
  | `45674 <https:////gerrit.fd.io/r/c/vpp/+/45674>`_ [vEC 1]: dhcp: export DHCPv6 runtime state for PPPoE observability
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [vEC 1]: rdma: steer PPPoE discovery and session flows

**Jing Peng** <jing@meter.com>:

  | `37058 <https:////gerrit.fd.io/r/c/vpp/+/37058>`_ [VeC 123]: vppapigen: fix json build error

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 65]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 65]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Klement Sekera** <ksekera@netgate.com>:

  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [vEC 0]: api: add build-time python stub generation via vppapigen
  | `46004 <https:////gerrit.fd.io/r/c/vpp/+/46004>`_ [vEC 2]: l2: don't let the fib scan clobber the learn count mid-learning
  | `46003 <https:////gerrit.fd.io/r/c/vpp/+/46003>`_ [vEC 2]: tests: allocate whole physical cores, not logical CPUs
  | `46002 <https:////gerrit.fd.io/r/c/vpp/+/46002>`_ [vEC 2]: tests: extract systemd-coredump cores via coredumpctl
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 46]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [VEc 10]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route
  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [VEc 11]: ipip: add mp2p ipip tunnel

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [vEc 3]: flow: add per-thread flow pool cache for multi-worker safety
  | `45000 <https:////gerrit.fd.io/r/c/vpp/+/45000>`_ [vEc 3]: flow: add flow template and async range infrastructure
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vEC 3]: dpdk: support async flow offload
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [vEC 3]: dpdk: multi-thread async flow offload with per-worker caches
  | `45296 <https:////gerrit.fd.io/r/c/vpp/+/45296>`_ [VeC 76]: ethernet: implement outer_vlan_id_any sub-interface matching
  | `45280 <https:////gerrit.fd.io/r/c/vpp/+/45280>`_ [VeC 76]: gso: implement IPv6 extension header traversal
  | `45249 <https:////gerrit.fd.io/r/c/vpp/+/45249>`_ [VeC 82]: policer: fix DSCP marking for VLAN-tagged packets
  | `45252 <https:////gerrit.fd.io/r/c/vpp/+/45252>`_ [VeC 82]: policer: fix unchecked policer removal
  | `45253 <https:////gerrit.fd.io/r/c/vpp/+/45253>`_ [veC 82]: policer: reject delete of policer still applied to interface
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VeC 82]: policer: reject deletion of policer used by punt policing

**Mohammad Mahdi Nemati Haravani** <nemati.mahdi255@gmail.com>:

  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [vEC 16]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 179]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 61]: snort: copy metadata from original to generated packets
  | `44919 <https:////gerrit.fd.io/r/c/vpp/+/44919>`_ [VeC 81]: snort: fix inject/finalize ordering race in deq node
  | `45177 <https:////gerrit.fd.io/r/c/vpp/+/45177>`_ [VeC 87]: sfdp: add blacklist/whitelist to snort service
  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [VeC 110]: ipip: fix support for ipip6o6 from linux tunnel
  | `44715 <https:////gerrit.fd.io/r/c/vpp/+/44715>`_ [Vec 114]: pg: Guard against non‑monotonic time and negative accumulator
  | `44426 <https:////gerrit.fd.io/r/c/vpp/+/44426>`_ [VeC 149]: virtio: add the check if MAC feature is negotiated

**Moinak Bhattacharyya** <moinakb001@gmail.com>:

  | `44708 <https:////gerrit.fd.io/r/c/vpp/+/44708>`_ [VeC 127]: iouring: Add io_uring plugin to allow polling usage of io_uring

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VeC 60]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VeC 60]: ip6-nd: add nd-proxy all dst
  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 68]: ip6: fix show ip6-ll cli if selector
  | `44903 <https:////gerrit.fd.io/r/c/vpp/+/44903>`_ [VeC 104]: vxlan: reset next_dpo on delete
  | `44961 <https:////gerrit.fd.io/r/c/vpp/+/44961>`_ [Vec 109]: ip6-nd: support RA pfx info option with flag L&!A

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vEc 3]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 53]: papi: improve performance on set_errors

**Parth Sahu** <parthsahu15@gmail.com>:

  | `44813 <https:////gerrit.fd.io/r/c/vpp/+/44813>`_ [VeC 129]: session auto_sdl: fix SDL show rule argument order
  | `44796 <https:////gerrit.fd.io/r/c/vpp/+/44796>`_ [veC 130]: fix: correct fixstyle in session_sdl command function

**Pim van Pelt** <pim@ipng.nl>:

  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 60]: lb: Add punt feature to per-port VIPs

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [VEc 11]: pfc: add framework for priority flow control

**Robert Shearman** <robertshearman@gmail.com>:

  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [VeC 37]: vppapigen: fix inconsistency in paths JSON

**Samuel Benko** <sbenko@cisco.com>:

  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [vEc 2]: tls: propagate verify config for dtls
  | `45961 <https:////gerrit.fd.io/r/c/vpp/+/45961>`_ [vEC 2]: hsa: handle echo client session closes/resets
  | `45766 <https:////gerrit.fd.io/r/c/vpp/+/45766>`_ [vEC 2]: hs-test: add dtls crl reject allow test
  | `45858 <https:////gerrit.fd.io/r/c/vpp/+/45858>`_ [VEc 2]: hsa: fix builtin echo cut-through

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `45917 <https:////gerrit.fd.io/r/c/vpp/+/45917>`_ [VEc 4]: linux-cp: mcast ospf test
  | `44230 <https:////gerrit.fd.io/r/c/vpp/+/44230>`_ [veC 68]: linux-cp: bind lcp_router_table lifetime to lcp_itf_pair
  | `44232 <https:////gerrit.fd.io/r/c/vpp/+/44232>`_ [VeC 163]: linux-cp: fix cleanup of special routes
  | `44241 <https:////gerrit.fd.io/r/c/vpp/+/44241>`_ [Vec 171]: linux-cp: on remove do cleanup for all fibs

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [VEc 20]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 68]: vppinfra: collect heap stats in constant time

**Vladislav Grishenko** <themiron@mail.ru>:

  | `44575 <https:////gerrit.fd.io/r/c/vpp/+/44575>`_ [VeC 149]: fib: add interface-rx dpo mpls support
  | `44574 <https:////gerrit.fd.io/r/c/vpp/+/44574>`_ [VeC 149]: fib: fix stale interface-rx dpo fib after deag/lookup
  | `41660 <https:////gerrit.fd.io/r/c/vpp/+/41660>`_ [VeC 149]: nat: add nat44-ed ipfix dst address and port logging
  | `42538 <https:////gerrit.fd.io/r/c/vpp/+/42538>`_ [VeC 149]: nat: speedup nat44-ed vrf table lookups
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 149]: nat: fix nat44-ed address removal from fib
  | `44563 <https:////gerrit.fd.io/r/c/vpp/+/44563>`_ [veC 150]: ip: fix DSCP CS7 value
  | `44568 <https:////gerrit.fd.io/r/c/vpp/+/44568>`_ [VeC 150]: vxlan: add default dscp value config for vxlan encap
  | `44567 <https:////gerrit.fd.io/r/c/vpp/+/44567>`_ [VeC 150]: udp: add default dscp value config for udp encap
  | `40627 <https:////gerrit.fd.io/r/c/vpp/+/40627>`_ [VeC 150]: fib: fix invalid udp encap id cases
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 150]: fib: fix udp encap mp-safe ops and id validation
  | `43180 <https:////gerrit.fd.io/r/c/vpp/+/43180>`_ [VeC 150]: fib: avoid loadbalance dpo node path polarisation
  | `40630 <https:////gerrit.fd.io/r/c/vpp/+/40630>`_ [VeC 150]: vlib: mark cli quit command as mp_safe

**Vratko Polak** <vrpolak@cisco.com>:

  | `45953 <https:////gerrit.fd.io/r/c/vpp/+/45953>`_ [vEC 2]: iavf: ensure wb_on_itr in poll mode
  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vEc 9]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 53]: empty change for GHA(CSIT) testing

**Wayne Morrison** <wmorrison@netgate.com>:

  | `45949 <https:////gerrit.fd.io/r/c/vpp/+/45949>`_ [vEc 2]: lldp: extend data returned by lldp-dump API

**Xiangqing Cheng** <chengxq@chinatelecom.cn>:

  | `42849 <https:////gerrit.fd.io/r/c/vpp/+/42849>`_ [VeC 165]: ip-neighbor: ARP/NA per-interface counter improvements

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [VEc 11]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [vEC 12]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vEc 18]: vlib: pre-input node should be dispatched before input node

**echo** <614699596@qq.com>:

  | `45348 <https:////gerrit.fd.io/r/c/vpp/+/45348>`_ [VeC 73]: bpf_trace_filter: fix bpf_expr memory leak on error path

**joydeep ghosh** <joydeep779@gmail.com>:

  | `44631 <https:////gerrit.fd.io/r/c/vpp/+/44631>`_ [vec 117]: dns: fix crash when no usable source address exists

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [vEC 27]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 68]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 68]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 69]: build rpm-packaging: make vpp rpm package for kylinV11
  | `42064 <https:////gerrit.fd.io/r/c/vpp/+/42064>`_ [vec 122]: docs: Python apis examples

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 42]: fib: compute fib entry flags from full path list

**nleblanc** <nleblanc@joustsec.com>:

  | `45271 <https:////gerrit.fd.io/r/c/vpp/+/45271>`_ [VeC 80]: linux-cp: prevent MAC address sync on non-Ethernet interfaces on RTM_NEWLINK

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 68]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 68]: lb: fix API byte order and IPv4 prefix length handling
  | `44207 <https:////gerrit.fd.io/r/c/vpp/+/44207>`_ [VeC 162]: lb: fix incorrect byte order conversion for vip port display

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 37]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [VEc 27]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 33]: session: make transport to use application's segment manager
  | `44569 <https:////gerrit.fd.io/r/c/vpp/+/44569>`_ [VeC 150]: vppinfra: clib_time_verify_frequency may cause time jump

**yelena_c@rad.com** <yelena_c@rad.com>:

  | `44536 <https:////gerrit.fd.io/r/c/vpp/+/44536>`_ [veC 132]: hs-test: fix CI infra issues
  | `44421 <https:////gerrit.fd.io/r/c/vpp/+/44421>`_ [VeC 132]: l2: fix null pointer access in l2-efp-filter

**yewtow** <offside.items03@icloud.com>:

  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [VeC 55]: ip6-nd: update secondary RA prefixes for subnets
  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [VeC 56]: ip6-nd: support RDNSS option in IPv6 RA

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
authors          135
maintainers      54
committers       3
abandoned        0
================ ===

