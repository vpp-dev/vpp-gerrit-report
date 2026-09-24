
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Thursday 2026-09-24, 06:08:39
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

  | `46634 <https:////gerrit.fd.io/r/c/vpp/+/46634>`_ [VECR 14]: tests: preserve timeout diagnostics across retries
  | `46657 <https:////gerrit.fd.io/r/c/vpp/+/46657>`_ [VECR 14]: nat: tolerate unchanged translated ports
  | `46636 <https:////gerrit.fd.io/r/c/vpp/+/46636>`_ [VECR 19]: tests: avoid repeated pg barriers awaiting capture

Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `46481 <https:////gerrit.fd.io/r/c/vpp/+/46481>`_ [VECr 15]: acl: add callback hooks for list add/del

bier: **Neale Ranns** <neale@graphiant.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

bonding: **Steven Luong** <sluong@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 1]: vlib: ASAN-poison unallocated buffers
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 5]: buffers: make natural layout always default

build: **Damjan Marion** <damarion@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 5]: buffers: make natural layout always default
  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VECr 8]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic

classify: **Dave Barach** <vpp@barachs.net>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `46753 <https:////gerrit.fd.io/r/c/vpp/+/46753>`_ [VECr 0]: cnat: prevent SNAT policy aliasing across FIBs
  | `46809 <https:////gerrit.fd.io/r/c/vpp/+/46809>`_ [VECr 6]: cnat: skip output SNAT for unsupported protocols
  | `46760 <https:////gerrit.fd.io/r/c/vpp/+/46760>`_ [VECr 14]: cnat: do not count unsupported IP protocols as session alloc failure

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

dev: **Damjan Marion** <damarion@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46282 <https:////gerrit.fd.io/r/c/vpp/+/46282>`_ [VECr 4]: dev: advertise TX UDP GSO

devices: **Damjan Marion** <damarion@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 5]: pppoeclient: add PPPoE client plugin with DHCPv6 observability

dispatch-trace: **Dave Barach** <vpp@barachs.net>
  | `46469 <https:////gerrit.fd.io/r/c/vpp/+/46469>`_ [VECr 24]: dispatch-trace: fix SIGSEGV/SIGABRT on multi-worker handoff

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [VECr 1]: misc: surs patch to test CI infra
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 1]: misc: patch to test CI infra
  | `46808 <https:////gerrit.fd.io/r/c/vpp/+/46808>`_ [VECr 2]: docs: announce libvnet visibility change
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 4]: iavf: add setup documentation
  | `46727 <https:////gerrit.fd.io/r/c/vpp/+/46727>`_ [VECr 5]: ipsec: IPTFS (RFC 9347) plugin (encap, decap, timing)
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 5]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 5]: buffers: make natural layout always default
  | `46075 <https:////gerrit.fd.io/r/c/vpp/+/46075>`_ [VECr 7]: docs: update tsc vulnerability management process
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 7]: rdma: add mlx5 DV TSO support for raw packet tx
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 14]: teib: move the TEIB implementation to a plugin
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 28]: sfdp: add sfdp-session-stats service

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `45675 <https:////gerrit.fd.io/r/c/vpp/+/45675>`_ [VECr 5]: dpdk: log MFIB MAC replay tolerance at debug level

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

feature: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

fib: **Neale Ranns** <neale@graphiant.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

flow: **Damjan Marion** <damarion@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

hash: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `46723 <https:////gerrit.fd.io/r/c/vpp/+/46723>`_ [VECr 1]: hsi: wake drains when ownership changes

hsi: **Florin Coras** <fcoras@cisco.com>
  | `46723 <https:////gerrit.fd.io/r/c/vpp/+/46723>`_ [VECr 1]: hsi: wake drains when ownership changes

iavf: **Damjan Marion** <damarion@cisco.com>
  | `45159 <https:////gerrit.fd.io/r/c/vpp/+/45159>`_ [VECr 1]: iavf: fix native TSO datapath
  | `46271 <https:////gerrit.fd.io/r/c/vpp/+/46271>`_ [VECr 4]: iavf: fix iavf_tx_fill_ctx_desc ph buf seg fault
  | `46283 <https:////gerrit.fd.io/r/c/vpp/+/46283>`_ [VECr 4]: iavf: add UDP segmentation offload support
  | `46261 <https:////gerrit.fd.io/r/c/vpp/+/46261>`_ [VECr 4]: iavf: fix rx queue max_pkt_size value set on init
  | `46262 <https:////gerrit.fd.io/r/c/vpp/+/46262>`_ [VECr 4]: iavf: add setup documentation

interface: **Dave Barach** <vpp@barachs.net>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 5]: pppoeclient: fix orphan TX nodes and shared rename
  | `46651 <https:////gerrit.fd.io/r/c/vpp/+/46651>`_ [VECr 20]: vnet: keep deleted interface node names unique

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46865 <https:////gerrit.fd.io/r/c/vpp/+/46865>`_ [VECr 0]: ip: include ICMP Echo identifiers in flow hashes
  | `46051 <https:////gerrit.fd.io/r/c/vpp/+/46051>`_ [VECr 1]: ip: fix punt socket rx when multiple FDs are ready
  | `45954 <https:////gerrit.fd.io/r/c/vpp/+/45954>`_ [VECr 1]: ip: fix adjacent packet overwrite with ip6 frags
  | `45955 <https:////gerrit.fd.io/r/c/vpp/+/45955>`_ [VECr 1]: ip: fix adjacent packet overwrite with ip frags
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 1]: ip: fix ip mroute bulk insertion CLI for certain inputs

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 12]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 12]: ip6-nd: add nd-proxy all dst
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 12]: ip6-nd: fix unicast NA handling in ND proxy

ipfix-export: **Ole Troan** <otroan@employees.org>, **Paul Atkins** <patkins@graphiant.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

ipip: **Ole Troan** <otroan@employees.org>
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 14]: teib: move the TEIB implementation to a plugin

ipsec: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 14]: teib: move the TEIB implementation to a plugin

kube-test: **Florin Coras** <fcoras@cisco.com>
  | `46593 <https:////gerrit.fd.io/r/c/vpp/+/46593>`_ [VECr 22]: tests: bypass http/https proxy in test curl invocations

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `46796 <https:////gerrit.fd.io/r/c/vpp/+/46796>`_ [VECr 1]: lb: use portable vectors for sticky lookup

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46727 <https:////gerrit.fd.io/r/c/vpp/+/46727>`_ [VECr 5]: ipsec: IPTFS (RFC 9347) plugin (encap, decap, timing)
  | `46749 <https:////gerrit.fd.io/r/c/vpp/+/46749>`_ [VECr 5]: pppoeclient: fix orphan TX nodes and shared rename
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 5]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `44303 <https:////gerrit.fd.io/r/c/vpp/+/44303>`_ [VECr 8]: build: fix etc path for vpp-ext-deps package fix the bug vpp ext deb for DPDK 25.07 and MLX5 PMD topic
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 14]: teib: move the TEIB implementation to a plugin

mpls: **Neale Ranns** <neale@graphiant.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

papi: **Ole Troan** <otroan@employees.org>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46555 <https:////gerrit.fd.io/r/c/vpp/+/46555>`_ [VECr 27]: papi: use public ipaddress .version (Python 3.14/Ubuntu 26.04)

pg: **Dave Barach** <vpp@barachs.net>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

quic: **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Florin Coras** <fcoras@cisco.com>
  | `46315 <https:////gerrit.fd.io/r/c/vpp/+/46315>`_ [VECr 4]: quic: quic_quicly add uso support

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `45676 <https:////gerrit.fd.io/r/c/vpp/+/45676>`_ [VECr 5]: rdma: steer PPPoE discovery and session flows
  | `45505 <https:////gerrit.fd.io/r/c/vpp/+/45505>`_ [VECr 7]: rdma: add mlx5 DV TSO support for raw packet tx
  | `46465 <https:////gerrit.fd.io/r/c/vpp/+/46465>`_ [VECr 7]: rdma: add mlx5 enhanced MPW with optional inline

session: **Florin Coras** <fcoras@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 4]: udp: add segmentation offload support
  | `46797 <https:////gerrit.fd.io/r/c/vpp/+/46797>`_ [VECr 7]: session: report refused for local connect miss
  | `46473 <https:////gerrit.fd.io/r/c/vpp/+/46473>`_ [VECr 13]: session: revalidate ct listener during accept

sfdp: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Ole Troan** <otroan@employees.org>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46362 <https:////gerrit.fd.io/r/c/vpp/+/46362>`_ [VECr 22]: sfdp: add api sfdp_kill_session_batch

sfdp_services: **Mohammed Hawari** <mohammed@hawari.fr>, **Hadi Rayan Al-Sandid** <halsandi@cisco.com>, **Guillaume Solignac** <gsoligna@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 28]: sfdp: add sfdp-session-stats service

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

syslog: **Matus Fabian** <matfabia@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

tcp: **Florin Coras** <fcoras@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

teib: **Neale Ranns** <neale@graphiant.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 14]: teib: move the TEIB implementation to a plugin

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `46865 <https:////gerrit.fd.io/r/c/vpp/+/46865>`_ [VECr 0]: ip: include ICMP Echo identifiers in flow hashes
  | `46753 <https:////gerrit.fd.io/r/c/vpp/+/46753>`_ [VECr 0]: cnat: prevent SNAT policy aliasing across FIBs
  | `45957 <https:////gerrit.fd.io/r/c/vpp/+/45957>`_ [VECr 1]: vlib: ASAN-poison unallocated buffers
  | `46050 <https:////gerrit.fd.io/r/c/vpp/+/46050>`_ [VECr 1]: ip: fix ip mroute bulk insertion CLI for certain inputs
  | `46728 <https:////gerrit.fd.io/r/c/vpp/+/46728>`_ [VECr 5]: ipsec: IPTFS (RFC 9347) unit tests
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 5]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46809 <https:////gerrit.fd.io/r/c/vpp/+/46809>`_ [VECr 6]: cnat: skip output SNAT for unsupported protocols
  | `46780 <https:////gerrit.fd.io/r/c/vpp/+/46780>`_ [VECr 11]: tests: extend BFD peer detection window
  | `45046 <https:////gerrit.fd.io/r/c/vpp/+/45046>`_ [VECr 12]: ip6-nd: add punt reason for neigh advs
  | `45099 <https:////gerrit.fd.io/r/c/vpp/+/45099>`_ [VECr 12]: ip6-nd: add nd-proxy all dst
  | `44350 <https:////gerrit.fd.io/r/c/vpp/+/44350>`_ [VECr 12]: ip6-nd: fix unicast NA handling in ND proxy
  | `46541 <https:////gerrit.fd.io/r/c/vpp/+/46541>`_ [VECr 14]: tests: preserve LD_PRELOAD across stdbuf on uutils (Rust)
  | `46554 <https:////gerrit.fd.io/r/c/vpp/+/46554>`_ [VECr 14]: tests: fix multiprocessing Python 3.14 failures on Ubuntu 26.04
  | `46760 <https:////gerrit.fd.io/r/c/vpp/+/46760>`_ [VECr 14]: cnat: do not count unsupported IP protocols as session alloc failure
  | `46640 <https:////gerrit.fd.io/r/c/vpp/+/46640>`_ [VECr 14]: tests: tolerate delayed BFD observations
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 14]: teib: move the TEIB implementation to a plugin
  | `46651 <https:////gerrit.fd.io/r/c/vpp/+/46651>`_ [VECr 20]: vnet: keep deleted interface node names unique
  | `46719 <https:////gerrit.fd.io/r/c/vpp/+/46719>`_ [VECr 20]: tests: avoid iperf preexec deadlocks
  | `46720 <https:////gerrit.fd.io/r/c/vpp/+/46720>`_ [VECr 20]: tests: make qemu network lock recoverable
  | `46593 <https:////gerrit.fd.io/r/c/vpp/+/46593>`_ [VECr 22]: tests: bypass http/https proxy in test curl invocations
  | `46362 <https:////gerrit.fd.io/r/c/vpp/+/46362>`_ [VECr 22]: sfdp: add api sfdp_kill_session_batch
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 28]: sfdp: add sfdp-session-stats service

tls: **Florin Coras** <fcoras@cisco.com>, **Ping Yu** <ping.yu@intel.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

udp: **Florin Coras** <fcoras@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports
  | `46284 <https:////gerrit.fd.io/r/c/vpp/+/46284>`_ [VECr 4]: udp: add segmentation offload support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `46797 <https:////gerrit.fd.io/r/c/vpp/+/46797>`_ [VECr 7]: session: report refused for local connect miss
  | `46625 <https:////gerrit.fd.io/r/c/vpp/+/46625>`_ [VECr 14]: teib: move the TEIB implementation to a plugin

vcl: **Florin Coras** <fcoras@cisco.com>
  | `46516 <https:////gerrit.fd.io/r/c/vpp/+/46516>`_ [VECr 1]: misc: surs patch to test CI infra
  | `45941 <https:////gerrit.fd.io/r/c/vpp/+/45941>`_ [VECr 1]: misc: patch to test CI infra

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `46800 <https:////gerrit.fd.io/r/c/vpp/+/46800>`_ [VECr 0]: vlib: pool-cache prefill and foreach macro
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 5]: buffers: make natural layout always default
  | `46788 <https:////gerrit.fd.io/r/c/vpp/+/46788>`_ [VECr 9]: vlib: add show handoff pending CLI

vnet: **Damjan Marion** <damarion@cisco.com>
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

vpp: **Dave Barach** <vpp@barachs.net>
  | `45678 <https:////gerrit.fd.io/r/c/vpp/+/45678>`_ [VECr 5]: pppoeclient: add PPPoE client plugin with DHCPv6 observability
  | `46703 <https:////gerrit.fd.io/r/c/vpp/+/46703>`_ [VECr 5]: buffers: make natural layout always default
  | `44803 <https:////gerrit.fd.io/r/c/vpp/+/44803>`_ [VECr 28]: sfdp: add sfdp-session-stats service

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `46866 <https:////gerrit.fd.io/r/c/vpp/+/46866>`_ [VECr 0]: vppinfra: add the libunwind include dir
  | `46573 <https:////gerrit.fd.io/r/c/vpp/+/46573>`_ [VECr 0]: vnet: use hidden visibility with explicit exports

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Akeel Ali** <akeelapi@gmail.com>:

  | `45686 <https:////gerrit.fd.io/r/c/vpp/+/45686>`_ [Vec 100]: ip_validate: new plugin to drop packets with invalid addresses

**Akos Orban** <orbanakos2001@gmail.com>:

  | `44995 <https:////gerrit.fd.io/r/c/vpp/+/44995>`_ [VeC 107]: cnat: fix show cnat client showing invalid for client id
  | `45001 <https:////gerrit.fd.io/r/c/vpp/+/45001>`_ [VeC 107]: cnat: fix show cnat translation for specific translation id

**Alexander Chernavin** <chernavin@mts.ru>:

  | `43726 <https:////gerrit.fd.io/r/c/vpp/+/43726>`_ [vEc 23]: vhost: fix rxvq interrupts triggered because of race

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `45877 <https:////gerrit.fd.io/r/c/vpp/+/45877>`_ [VeC 124]: snort: don't store snort metadata in buffer

**Anil Kainikara** <anilkumar911@gmail.com>:

  | `46256 <https:////gerrit.fd.io/r/c/vpp/+/46256>`_ [vec 69]: crypto: openssl - check ctx alloc/init in key-add
  | `45663 <https:////gerrit.fd.io/r/c/vpp/+/45663>`_ [VeC 147]: map: enhance map plugin to support per-vrf rules

**Anton Blazhko** <ablazhko@cisco.com>:

  | `45808 <https:////gerrit.fd.io/r/c/vpp/+/45808>`_ [Vec 70]: devices: Convert PIPE to plugin

**Aritra Basu** <aritrbas@cisco.com>:

  | `46530 <https:////gerrit.fd.io/r/c/vpp/+/46530>`_ [VeC 34]: gha: skip build/test verify jobs for docs-only changes
  | `45705 <https:////gerrit.fd.io/r/c/vpp/+/45705>`_ [Vec 78]: kube-test: support CalicoVPP repo restructure (backward-compatible)
  | `46048 <https:////gerrit.fd.io/r/c/vpp/+/46048>`_ [VeC 85]: tcp: add TCP fast open support (RFC 7413)
  | `46167 <https:////gerrit.fd.io/r/c/vpp/+/46167>`_ [veC 89]: kube-test: retry Job finalizer cleanup conflicts
  | `45536 <https:////gerrit.fd.io/r/c/vpp/+/45536>`_ [VeC 103]: interface: enable IPv6 link state on unnumbered interfaces
  | `45583 <https:////gerrit.fd.io/r/c/vpp/+/45583>`_ [VeC 103]: vlib: fix trace flag loss when multiple pending frames share next frame

**Benoît Ganne** <bganne@cisco.com>:

  | `46368 <https:////gerrit.fd.io/r/c/vpp/+/46368>`_ [VeC 57]: vppinfra: make vec_foreach_pointer empty-safe
  | `46117 <https:////gerrit.fd.io/r/c/vpp/+/46117>`_ [VeC 93]: vppapigen: fix vppapigen depfile without imports
  | `46087 <https:////gerrit.fd.io/r/c/vpp/+/46087>`_ [VeC 93]: cnat: wait for cnat scanner session cleanup

**Damjan Marion** <dmarion@0xa5.net>:

  | `45409 <https:////gerrit.fd.io/r/c/vpp/+/45409>`_ [veC 110]: ikev2: add Curve25519 and Curve448 DH groups

**Dennis Lanov** <dennis.lanov@gmail.com>:

  | `46270 <https:////gerrit.fd.io/r/c/vpp/+/46270>`_ [VeC 70]: acl: correct interface command help

**Florin Coras** <florin.coras@gmail.com>:

  | `46831 <https:////gerrit.fd.io/r/c/vpp/+/46831>`_ [vEC 0]: nsim: add reproducible variable-rate simulation
  | `46687 <https:////gerrit.fd.io/r/c/vpp/+/46687>`_ [vEC 22]: vppinfra: avoid duplicate rbtree custom comparison

**G. Paul Ziemba** <pz-vpp-dev@ziemba.us>:

  | `46461 <https:////gerrit.fd.io/r/c/vpp/+/46461>`_ [VEc 5]: ipsec: IPTFS (RFC 9347) foundation
  | `45510 <https:////gerrit.fd.io/r/c/vpp/+/45510>`_ [vEC 18]: crypto: add op tracing capability
  | `45699 <https:////gerrit.fd.io/r/c/vpp/+/45699>`_ [VeC 47]: dpdk: buffer bug fixes
  | `45683 <https:////gerrit.fd.io/r/c/vpp/+/45683>`_ [Vec 140]: dpdk: tracing improvements

**GregMiller** <greg@gregmiller.co.za>:

  | `46129 <https:////gerrit.fd.io/r/c/vpp/+/46129>`_ [VeC 92]: pppoe: native per-session rx policing in pppoe-decap node
  | `46125 <https:////gerrit.fd.io/r/c/vpp/+/46125>`_ [VeC 92]: pppoe: add combined subscriber session provisioning API

**Hadi Rayan Al-Sandid** <halsandi@cisco.com>:

  | `46588 <https:////gerrit.fd.io/r/c/vpp/+/46588>`_ [vEC 23]: sfdp_services: various sfdp nat improvements
  | `44847 <https:////gerrit.fd.io/r/c/vpp/+/44847>`_ [VeC 84]: sfdp: modify tenant_index type from u16 to u32
  | `45964 <https:////gerrit.fd.io/r/c/vpp/+/45964>`_ [VeC 91]: flow: add parameter to pre-allocate global pool
  | `45481 <https:////gerrit.fd.io/r/c/vpp/+/45481>`_ [veC 91]: flow: add action VNET_FLOW_ACTION_STEER_TO_PORT
  | `45637 <https:////gerrit.fd.io/r/c/vpp/+/45637>`_ [VeC 91]: dpdk: add support for VNET_FLOW_ACTION_AGE action
  | `45633 <https:////gerrit.fd.io/r/c/vpp/+/45633>`_ [veC 91]: dpdk: add support for represented port action
  | `45482 <https:////gerrit.fd.io/r/c/vpp/+/45482>`_ [Vec 92]: sfdp: add verdict-testbench service
  | `46043 <https:////gerrit.fd.io/r/c/vpp/+/46043>`_ [VeC 92]: flow: add APIs to support new flow actions
  | `45636 <https:////gerrit.fd.io/r/c/vpp/+/45636>`_ [VeC 92]: flow: add flow aging support
  | `45635 <https:////gerrit.fd.io/r/c/vpp/+/45635>`_ [VeC 104]: dpdk: add support for VNET_FLOW_ACTION_COUNT
  | `45634 <https:////gerrit.fd.io/r/c/vpp/+/45634>`_ [VeC 104]: flow: implement VNET_FLOW_ACTION_COUNT operation
  | `45938 <https:////gerrit.fd.io/r/c/vpp/+/45938>`_ [Vec 107]: tracepath: minor refactoring to code
  | `45848 <https:////gerrit.fd.io/r/c/vpp/+/45848>`_ [VeC 128]: sfdp: fix specification of scope_index

**Hanataba Azaka** <northern.snow.x@gmail.com>:

  | `46041 <https:////gerrit.fd.io/r/c/vpp/+/46041>`_ [VeC 93]: cnat: make session scanner budget configurable

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `46147 <https:////gerrit.fd.io/r/c/vpp/+/46147>`_ [Vec 89]: npol: support prednat policies
  | `45914 <https:////gerrit.fd.io/r/c/vpp/+/45914>`_ [Vec 93]: cnat: preallocate ts_pools to eliminate reader locks on timestamp get

**Ivan Shvedunov** <ishvedunov@netgate.com>:

  | `46338 <https:////gerrit.fd.io/r/c/vpp/+/46338>`_ [VeC 42]: fib: tolerate a NULL rewrite in vnet_rewrite_for_sw_interface
  | `46339 <https:////gerrit.fd.io/r/c/vpp/+/46339>`_ [VeC 42]: abf: reject attachment to a non-existent policy instead of asserting

**Janik** <janik.haag@imc.com>:

  | `46122 <https:////gerrit.fd.io/r/c/vpp/+/46122>`_ [Vec 64]: build: fix make install-deps for fedora targets
  | `46123 <https:////gerrit.fd.io/r/c/vpp/+/46123>`_ [VeC 93]: vcl: add regression test for nonblocking connect()
  | `46124 <https:////gerrit.fd.io/r/c/vpp/+/46124>`_ [VeC 93]: vcl: add regression test for ignorable flags
  | `46121 <https:////gerrit.fd.io/r/c/vpp/+/46121>`_ [VeC 93]: sasc: fix gcc uninitialized warning

**Jerome Tollet** <jtollet@cisco.com>:

  | `46280 <https:////gerrit.fd.io/r/c/vpp/+/46280>`_ [VEc 1]: svm: allow fifo chunk provisioning at offset
  | `45759 <https:////gerrit.fd.io/r/c/vpp/+/45759>`_ [VeC 134]: tcp: support chained buffers in GRO
  | `45764 <https:////gerrit.fd.io/r/c/vpp/+/45764>`_ [VeC 134]: tcp: allow selective GRO enablement
  | `44572 <https:////gerrit.fd.io/r/c/vpp/+/44572>`_ [VeC 148]: virtio: add native plugin L2 xconnect test with QEMU

**Jianquan Ye** <jianquanye@microsoft.com>:

  | `45864 <https:////gerrit.fd.io/r/c/vpp/+/45864>`_ [Vec 105]: ip bonding hash: inner-aware flow hash (opt-in)

**Justin Thomas** <justin@jdt.io>:

  | `45410 <https:////gerrit.fd.io/r/c/vpp/+/45410>`_ [VeC 173]: ct6: fix multi-worker session lookup and allow non-physical interfaces
  | `45411 <https:////gerrit.fd.io/r/c/vpp/+/45411>`_ [VeC 173]: ct6: move ct6-in2out from interface-output to ip6-unicast arc

**Keith Spinney** <kspinney@cisco.com>:

  | `46525 <https:////gerrit.fd.io/r/c/vpp/+/46525>`_ [VEc 29]: fib: barrier-protect fib_path_list_destroy()
  | `46526 <https:////gerrit.fd.io/r/c/vpp/+/46526>`_ [VeC 35]: lb: fix NAT66 UDP/IPv6 checksum zero-fold
  | `46527 <https:////gerrit.fd.io/r/c/vpp/+/46527>`_ [VeC 35]: lb: add NAT6_NOPORT encap type

**Klement Sekera** <ksekera@netgate.com>:

  | `46789 <https:////gerrit.fd.io/r/c/vpp/+/46789>`_ [vEC 9]: test: wait for handoff queues to drain before reading a capture
  | `46013 <https:////gerrit.fd.io/r/c/vpp/+/46013>`_ [VeC 71]: build: include GNUInstallDirs in VPPConfig
  | `45728 <https:////gerrit.fd.io/r/c/vpp/+/45728>`_ [VeC 71]: api: add build-time python stub generation via vppapigen
  | `45470 <https:////gerrit.fd.io/r/c/vpp/+/45470>`_ [VeC 154]: vppinfra: add cast to prevent warning

**Longxiang Lyu** <lolv@microsoft.com>:

  | `45685 <https:////gerrit.fd.io/r/c/vpp/+/45685>`_ [Vec 104]: ipip: add p2ap ipip tunnel
  | `45898 <https:////gerrit.fd.io/r/c/vpp/+/45898>`_ [Vec 104]: ip: add 'no-class-e-drop' startup config option to suppress class E drop route

**Matus Fabian** <mfabianlf@pm.me>:

  | `46579 <https:////gerrit.fd.io/r/c/vpp/+/46579>`_ [vEC 0]: misc: patch to test maketest action timeout

**Maxime Peim** <maxime.peim@gmail.com>:

  | `45578 <https:////gerrit.fd.io/r/c/vpp/+/45578>`_ [vEC 0]: flow: add per-thread flow pool cache for multi-worker safety
  | `45254 <https:////gerrit.fd.io/r/c/vpp/+/45254>`_ [VEc 9]: policer: reject deletion of policer used by punt policing
  | `45098 <https:////gerrit.fd.io/r/c/vpp/+/45098>`_ [vec 82]: dpdk: support async flow offload
  | `46032 <https:////gerrit.fd.io/r/c/vpp/+/46032>`_ [veC 105]: docs: document build-time VPP parameters
  | `45152 <https:////gerrit.fd.io/r/c/vpp/+/45152>`_ [VeC 111]: dpdk: install default jump-to-group-1 rule for mlx5
  | `45539 <https:////gerrit.fd.io/r/c/vpp/+/45539>`_ [veC 111]: dpdk: multi-thread async flow offload with per-worker caches

**Mohammed HAWARI** <momohawari@gmail.com>:

  | `42343 <https:////gerrit.fd.io/r/c/vpp/+/42343>`_ [VeC 33]: vcl: LDP default to regular option

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `42886 <https:////gerrit.fd.io/r/c/vpp/+/42886>`_ [Vec 37]: ipip: fix support for ipip6o6 from linux tunnel
  | `44923 <https:////gerrit.fd.io/r/c/vpp/+/44923>`_ [VeC 169]: snort: copy metadata from original to generated packets

**Mykyta Demusenko** <mdemusen@cisco.com>:

  | `46602 <https:////gerrit.fd.io/r/c/vpp/+/46602>`_ [VEc 14]: teib: narrow the C API and add a vnet-owned service boundary
  | `46724 <https:////gerrit.fd.io/r/c/vpp/+/46724>`_ [VEc 14]: teib: add tests for the TEIB API

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `44948 <https:////gerrit.fd.io/r/c/vpp/+/44948>`_ [VeC 176]: ip6: fix show ip6-ll cli if selector

**Nicolas PLANEL** <nplanel@gmail.com>:

  | `44976 <https:////gerrit.fd.io/r/c/vpp/+/44976>`_ [vec 111]: sfdp: async offload lookup

**Ole Troan** <otroan@employees.org>:

  | `46511 <https:////gerrit.fd.io/r/c/vpp/+/46511>`_ [vEC 20]: stats: add directory command to vpp_get_stats
  | `46434 <https:////gerrit.fd.io/r/c/vpp/+/46434>`_ [VeC 47]: vlib: fix log2 histogram overflow bin writing past the bin vector
  | `46380 <https:////gerrit.fd.io/r/c/vpp/+/46380>`_ [Vec 54]: vppapigen: fix unaligned access to packed messages
  | `45496 <https:////gerrit.fd.io/r/c/vpp/+/45496>`_ [Vec 161]: papi: improve performance on set_errors

**Onong Tayeng** <onong.tayeng@gmail.com>:

  | `46726 <https:////gerrit.fd.io/r/c/vpp/+/46726>`_ [VEc 0]: cnat: clear stale default SNAT policy pointer
  | `46752 <https:////gerrit.fd.io/r/c/vpp/+/46752>`_ [VEc 8]: cnat: update cnat plugin documentation
  | `46471 <https:////gerrit.fd.io/r/c/vpp/+/46471>`_ [VEc 12]: cnat: improve flow statistics and error coverage

**Pierre Pfister** <pierre@meter.com>:

  | `46857 <https:////gerrit.fd.io/r/c/vpp/+/46857>`_ [vEC 0]: vlib: initialize process sleep timer handle to ~0
  | `46858 <https:////gerrit.fd.io/r/c/vpp/+/46858>`_ [vEC 0]: vlib: resume a suspended process once per suspension

**Pim van Pelt** <pim@ipng.nl>:

  | `46038 <https:////gerrit.fd.io/r/c/vpp/+/46038>`_ [Vec 98]: ip6-nd: fix crash in link-local target NS
  | `45431 <https:////gerrit.fd.io/r/c/vpp/+/45431>`_ [VeC 168]: lb: Add punt feature to per-port VIPs

**Poornima Kandhade** <poornika@cisco.com>:

  | `46424 <https:////gerrit.fd.io/r/c/vpp/+/46424>`_ [vEC 7]: sfdp: add lifecycle records to session stats ring

**Qi Zhang** <zzqqqqwq77@gmail.com>:

  | `46458 <https:////gerrit.fd.io/r/c/vpp/+/46458>`_ [vEC 24]: vlib: detect freed buffer‑chain on node dispatch for double‑free debug
  | `46643 <https:////gerrit.fd.io/r/c/vpp/+/46643>`_ [vEC 24]: vnet: fix double-free in bcast fragment reassembly

**Rakesh Kudurumalla** <rkudurumalla@marvell.com>:

  | `45796 <https:////gerrit.fd.io/r/c/vpp/+/45796>`_ [Vec 119]: pfc: add framework for priority flow control
  | `45797 <https:////gerrit.fd.io/r/c/vpp/+/45797>`_ [VeC 131]: octeon: add PFC support

**Ram Subramanian** <ram@meter.com>:

  | `46442 <https:////gerrit.fd.io/r/c/vpp/+/46442>`_ [VeC 41]: vnet: install missing vnet headers

**Robert Shearman** <robertshearman@gmail.com>:

  | `44551 <https:////gerrit.fd.io/r/c/vpp/+/44551>`_ [vEC 1]: vppapigen: fix inconsistency in paths JSON
  | `46019 <https:////gerrit.fd.io/r/c/vpp/+/46019>`_ [vec 59]: misc: fix potential OOB read during flow hash calculations

**Samuel Benko** <sbenko@cisco.com>:

  | `45765 <https:////gerrit.fd.io/r/c/vpp/+/45765>`_ [VeC 91]: tls: propagate verify config for dtls

**Sergiy Bachynskyy** <sbachyns@cisco.com>:

  | `46206 <https:////gerrit.fd.io/r/c/vpp/+/46206>`_ [VeC 77]: ipfix: move to a plugin

**Shuzo Ichiyoshi** <deadcafe.beef@gmail.com>:

  | `46180 <https:////gerrit.fd.io/r/c/vpp/+/46180>`_ [VeC 50]: session: check event collector lookups
  | `46355 <https:////gerrit.fd.io/r/c/vpp/+/46355>`_ [VeC 57]: ip: fix fragmentation with negative buffer offset
  | `46178 <https:////gerrit.fd.io/r/c/vpp/+/46178>`_ [VeC 57]: session: validate app for async connect RPC
  | `46352 <https:////gerrit.fd.io/r/c/vpp/+/46352>`_ [VeC 59]: vppinfra: serialize VM map page size lookup
  | `46341 <https:////gerrit.fd.io/r/c/vpp/+/46341>`_ [VeC 61]: hsa: make TLS client CLI MP-safe
  | `46311 <https:////gerrit.fd.io/r/c/vpp/+/46311>`_ [VeC 63]: tcp: handle retransmitted SYN-ACK in TIME-WAIT

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `44249 <https:////gerrit.fd.io/r/c/vpp/+/44249>`_ [VEc 7]: fib: dump by src not only contributing routes

**Suresh Sundararaman** <suresh.serc@gmail.com>:

  | `46750 <https:////gerrit.fd.io/r/c/vpp/+/46750>`_ [VEc 6]: gha: add ubuntu2404-aarch64 debug and release jobs to periodic-vpp-verify-hst matrix
  | `46529 <https:////gerrit.fd.io/r/c/vpp/+/46529>`_ [VeC 34]: docs: Get the VPP Source

**Viacheslav Zakharchenko** <vzakharc@cisco.com>:

  | `45807 <https:////gerrit.fd.io/r/c/vpp/+/45807>`_ [Vec 70]: bfd: Introduce vppinfra/callback_data based vnet notifier for FIB/ADJ notifications
  | `45810 <https:////gerrit.fd.io/r/c/vpp/+/45810>`_ [Vec 71]: bfd: Extract to plugin

**Vladimir Lavor** <vlavor@cisco.com>:

  | `46268 <https:////gerrit.fd.io/r/c/vpp/+/46268>`_ [VeC 69]: vlib: expose error severity in stats segment

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `45650 <https:////gerrit.fd.io/r/c/vpp/+/45650>`_ [Vec 128]: flowprobe: count based sampling support

**Vladimir Zhigulin** <vladimir.jigulin@travelping.com>:

  | `40145 <https:////gerrit.fd.io/r/c/vpp/+/40145>`_ [veC 176]: vppinfra: collect heap stats in constant time

**Vratko Polak** <vrpolak@cisco.com>:

  | `45047 <https:////gerrit.fd.io/r/c/vpp/+/45047>`_ [vec 117]: sfdp_services: add basic support for time-wait
  | `45528 <https:////gerrit.fd.io/r/c/vpp/+/45528>`_ [veC 161]: empty change for GHA(CSIT) testing

**Wei Wang** <weiwa@cisco.com>:

  | `46085 <https:////gerrit.fd.io/r/c/vpp/+/46085>`_ [Vec 90]: tls: tls session resumption code and host stack tests

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `45901 <https:////gerrit.fd.io/r/c/vpp/+/45901>`_ [VeC 119]: vppinfra: fix use-after-poison issue in vec_foreach_pointer and pool_foreach_pointer
  | `45902 <https:////gerrit.fd.io/r/c/vpp/+/45902>`_ [Vec 119]: vppinfra: fix ASAN issue vec_len not thread safe
  | `45894 <https:////gerrit.fd.io/r/c/vpp/+/45894>`_ [veC 120]: vlib: vlib_node_rename should be guarded by thread barrier
  | `45895 <https:////gerrit.fd.io/r/c/vpp/+/45895>`_ [VeC 121]: vlib: fix process state format output wrapped by extra quotes
  | `45860 <https:////gerrit.fd.io/r/c/vpp/+/45860>`_ [vec 126]: vlib: pre-input node should be dispatched before input node

**Yang Liu** <numbksco@gmail.com>:

  | `46018 <https:////gerrit.fd.io/r/c/vpp/+/46018>`_ [Vec 82]: vppinfra: add loongarch64 architecture support

**Yuto Suzuki** <offside.items03@icloud.com>:

  | `45504 <https:////gerrit.fd.io/r/c/vpp/+/45504>`_ [Vec 63]: ip6-nd: support RDNSS option in IPv6 RA
  | `45503 <https:////gerrit.fd.io/r/c/vpp/+/45503>`_ [Vec 63]: ip6-nd: update secondary RA prefixes for subnets

**juhua yin** <ameliayin1990@gmail.com>:

  | `46828 <https:////gerrit.fd.io/r/c/vpp/+/46828>`_ [VEc 0]: dpdk: fix change mac address of the member failed

**lei feng** <1579628578@qq.com>:

  | `45761 <https:////gerrit.fd.io/r/c/vpp/+/45761>`_ [veC 135]: vlib: fix '\' command input will causes memory out of bounds
  | `42077 <https:////gerrit.fd.io/r/c/vpp/+/42077>`_ [Vec 176]: dns: dns request ip6 fix
  | `42129 <https:////gerrit.fd.io/r/c/vpp/+/42129>`_ [Vec 176]: dns: support ipv6 server to resolve name
  | `45374 <https:////gerrit.fd.io/r/c/vpp/+/45374>`_ [VeC 177]: build rpm-packaging: make vpp rpm package for kylinV11

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `43892 <https:////gerrit.fd.io/r/c/vpp/+/43892>`_ [VeC 150]: fib: compute fib entry flags from full path list

**niklesh** <nikleshparshaboina@gmail.com>:

  | `46546 <https:////gerrit.fd.io/r/c/vpp/+/46546>`_ [VeC 31]: vlib: re-base the timing wheel when arming an empty wheel
  | `45016 <https:////gerrit.fd.io/r/c/vpp/+/45016>`_ [veC 97]: cnat: add scope_id to session key

**peng xu** <84839011@sina.com>:

  | `44858 <https:////gerrit.fd.io/r/c/vpp/+/44858>`_ [VeC 176]: l2: fix missing CDP hello packets on BVI interface

**pkt4u** <pkt4u@outlook.com>:

  | `44208 <https:////gerrit.fd.io/r/c/vpp/+/44208>`_ [veC 176]: lb: fix API byte order and IPv4 prefix length handling

**shaohui jin** <jinshaohui789@163.com>:

  | `44928 <https:////gerrit.fd.io/r/c/vpp/+/44928>`_ [VeC 145]: fib: IPv4 Route Query Command Crash

**steven luong** <sluong@cisco.com>:

  | `45838 <https:////gerrit.fd.io/r/c/vpp/+/45838>`_ [VeC 132]: tls: add ALPN negotiation support
  | `45816 <https:////gerrit.fd.io/r/c/vpp/+/45816>`_ [VeC 134]: tls: fix picotls partial record handling
  | `45756 <https:////gerrit.fd.io/r/c/vpp/+/45756>`_ [Vec 135]: vcl: fix crash when closing listener with pending accepts
  | `44420 <https:////gerrit.fd.io/r/c/vpp/+/44420>`_ [Vec 141]: session: make transport to use application's segment manager

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
authors          140
maintainers      56
committers       3
abandoned        0
================ ===

