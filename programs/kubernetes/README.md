# Kubernetes

Disclosed reports: **77**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 2231019 | Code Injection | high | $5000 | [CVE-2023-5528: Insufficient input sanitization in in-tree storage plugin leads to privilege escalation on Windows nodes](2231019-cve-2023-5528-insufficient-input-sanitization-in-in-tree-sto.md) |
| 776017 | Server-Side Request Forgery (SSRF) | high | $5000 | [Half-Blind SSRF found in kube/cloud-controller-manager can be upgraded to complete SSRF (fully crafted HTTP requests) in vendor managed k8s service.](776017-half-blind-ssrf-found-in-kube-cloud-controller-manager-can-b.md) |
| 1580493 | Improper Authentication - Generic | high | $2500 | [Bypass validation parts in AWS IAM Authenticator for Kubernetes](1580493-bypass-validation-parts-in-aws-iam-authenticator-for-kuberne.md) |
| 1728174 | Code Injection | high | $2500 | [Ingress nginx annotation injection causes arbitrary command execution](1728174-ingress-nginx-annotation-injection-causes-arbitrary-command.md) |
| 1842829 | Privilege Escalation | high | $2500 | [Privilege Escalation in kOps using GCE/GCP Provider](1842829-privilege-escalation-in-kops-using-gce-gcp-provider.md) |
| 1620702 | Code Injection | high | $2500 | [RCE  on ingress-nginx-controller via Ingress spec.rules.http.paths.path field](1620702-rce-on-ingress-nginx-controller-via-ingress-spec-rules-http.md) |
| 2039464 | Code Injection | high | $2500 | [Code inject via nginx.ingress.kubernetes.io/permanent-redirect annotation](2039464-code-inject-via-nginx-ingress-kubernetes-io-permanent-redire.md) |
| 1382919 | Privilege Escalation | high | $2500 | [Ingress-nginx path allows retrieval of ingress-nginx serviceaccount token](1382919-ingress-nginx-path-allows-retrieval-of-ingress-nginx-service.md) |
| 867699 | Uncontrolled Resource Consumption | medium | $1000 | [Node disk DOS by writing to container /etc/hosts](867699-node-disk-dos-by-writing-to-container-etc-hosts.md) |
| 1544133 | Server-Side Request Forgery (SSRF) | medium | $1000 | [SSRF vulnerability can be exploited when a hijacked aggregated api server such as metrics-server returns 30X](1544133-ssrf-vulnerability-can-be-exploited-when-a-hijacked-aggregat.md) |
| 1167773 | Deserialization of Untrusted Data | medium | $1000 | [Loading YAML in Java client can lead to command execution](1167773-loading-yaml-in-java-client-can-lead-to-command-execution.md) |
| 1807214 | Code Injection | medium | $1000 | [The `io.kubernetes.client.util.generic.dynamic.Dynamics` contains a code execution vulnerability due to SnakeYAML](1807214-the-io-kubernetes-client-util-generic-dynamic-dynamics-conta.md) |
| 1032086 | NULL Pointer Dereference | medium | $500 | [csi-snapshot-controller crashes when processing VolumeSnapshot with non-existing PVC](1032086-csi-snapshot-controller-crashes-when-processing-volumesnapsh.md) |
| 1238017 | Resource Injection | medium | $500 | [AWS Load Balancer Controller Managed Security Groups can be replaced by an unprivileged attacker](1238017-aws-load-balancer-controller-managed-security-groups-can-be.md) |
| 1238482 | Resource Injection | medium | $500 | [AWS Load Balancer Controller can be used by an attacker to modify rules of any Security Group that they are able to tag](1238482-aws-load-balancer-controller-can-be-used-by-an-attacker-to-m.md) |
| 966383 | Cleartext Storage of Sensitive Information | medium | $500 | [secret leaks in vsphere cloud controller manager log](966383-secret-leaks-in-vsphere-cloud-controller-manager-log.md) |
| 1387366 | Cryptographic Issues - Generic | high | $250 | [elections.k8s.io uses weak session secret key, may place elections at risk](1387366-elections-k8s-io-uses-weak-session-secret-key-may-place-elec.md) |
| 746000 | Improper Authentication - Generic | medium | $250 | [Subdomain Takeover Via via Dangling NS records on Amazon Route 53 http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io](746000-subdomain-takeover-via-via-dangling-ns-records-on-amazon-rou.md) |
| 1485500 | Improper Access Control - Generic | medium | $250 | [File Read Vulnerability allows Attackers to Compromise S3 buckets using Prow](1485500-file-read-vulnerability-allows-attackers-to-compromise-s3-bu.md) |
| 1051192 | Code Injection | low | $250 | [Code Injection via Insecure Yaml.load](1051192-code-injection-via-insecure-yaml-load.md) |
| 1073363 | Buffer Over-read | none | $250 | [Index Out Of Bounds in protobuf unmarshalling](1073363-index-out-of-bounds-in-protobuf-unmarshalling.md) |
| 1466765 | Cross-Site Request Forgery (CSRF) | low | $100 | [monitoring.prow-canary.k8s.io is vulnerable to CVE-2022-21703 (Grafana 0-day)](1466765-monitoring-prow-canary-k8s-io-is-vulnerable-to-cve-2022-2170.md) |
| 1466889 | Insecure Temporary File | low | $100 | [Broken link hijacking in https://kubernetes-csi.github.io/docs/drivers.html?highlight=chubaofs#production-drivers](1466889-broken-link-hijacking-in-https-kubernetes-csi-github-io-docs.md) |
| 1434179 | Insecure Temporary File | low | $100 | [Broken Domain Link Takeover from kubernetes.io docs](1434179-broken-domain-link-takeover-from-kubernetes-io-docs.md) |
| 1763704 | Git Arg Injection in  kubernetes-sigs/release-sdk  | low | $100 | [Git Arg Injection in  kubernetes-sigs/release-sdk ](1763704-git-arg-injection-in-kubernetes-sigs-release-sdk.md) |
| 2701701 | Code Injection | high | $0 | [Injection in path parameter of Ingress-nginx](2701701-injection-in-path-parameter-of-ingress-nginx.md) |
| 1249583 | Privilege Escalation | high | $0 | [Authenticated kubernetes principal with restricted permissions can retrieve ingress-nginx serviceaccount token and secrets across all namespaces](1249583-authenticated-kubernetes-principal-with-restricted-permissio.md) |
| 1378175 | Code Injection | high | $0 | [Ingress-nginx annotation injection allows retrieval of ingress-nginx serviceaccount token and secrets across all namespaces](1378175-ingress-nginx-annotation-injection-allows-retrieval-of-ingre.md) |
| 1018413 | Cleartext Storage of Sensitive Information | high | $0 | [Development Application Credentials + Information Exposed](1018413-development-application-credentials-information-exposed.md) |
| 941178 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF for kube-apiserver cloudprovider scene](941178-ssrf-for-kube-apiserver-cloudprovider-scene.md) |
| 1434967 | Improper Access Control - Generic | low | $0 | [Github Account Takeover from Docs page of `kubernetes-csi.github.io`](1434967-github-account-takeover-from-docs-page-of-kubernetes-csi-git.md) |
| 1357948 | Improper Authentication - Generic | medium | $0 | [Attacker can bypass authentication build on ingress external auth (`nginx.ingress.kubernetes.io/auth-url`)](1357948-attacker-can-bypass-authentication-build-on-ingress-external.md) |
| 808169 | Server-Side Request Forgery (SSRF) | low | $0 | [Blind SSRF on velodrome.canary.k8s.io](808169-blind-ssrf-on-velodrome-canary-k8s-io.md) |
| 1398706 | Improper Access Control - Generic | medium | $0 | [Google storage bucket takeover which is used to load JS file in dashboard.html in "github.com/kubernetes/release" which can lead to XSS](1398706-google-storage-bucket-takeover-which-is-used-to-load-js-file.md) |
| 1095612 | Improper Access Control - Generic | medium | $0 | [Node Validation Admission does not observe all oldObject fields](1095612-node-validation-admission-does-not-observe-all-oldobject-fie.md) |
| 794382 | Misconfiguration | high | $0 | [Route53 Subdomain Takeover on test-cncf-aws.canary.k8s.io](794382-route53-subdomain-takeover-on-test-cncf-aws-canary-k8s-io.md) |
| 1331361 | Improper Access Control - Generic | low | $0 | [Broken Link Hijacking on kubernetes.io Documentation](1331361-broken-link-hijacking-on-kubernetes-io-documentation.md) |
| 776461 |  Username enumeration via Openssh 7.6 | medium | $0 | [ Username enumeration via Openssh 7.6](776461-username-enumeration-via-openssh-7-6.md) |
| 1130416 | Cryptographic Issues - Generic | medium | $0 | [SHA512 incorrect on most/many releases](1130416-sha512-incorrect-on-most-many-releases.md) |
| 819717 | Man-in-the-Middle | medium | $0 | [IPv4 only clusters susceptible to MitM attacks via IPv6 rogue router advertisements](819717-ipv4-only-clusters-susceptible-to-mitm-attacks-via-ipv6-rogu.md) |
| 863979 | Compromise of node can lead to compromise of pods on other nodes | medium | $0 | [Compromise of node can lead to compromise of pods on other nodes](863979-compromise-of-node-can-lead-to-compromise-of-pods-on-other-n.md) |
| 1073514 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [XSS on kubernetes-csi.github.io (mdBook)](1073514-xss-on-kubernetes-csi-github-io-mdbook.md) |
| 774896 | Uncontrolled Resource Consumption | medium | $0 | [Kubelet resource exhaustion attack via metric label cardinality explosion from unauthenticated requests](774896-kubelet-resource-exhaustion-attack-via-metric-label-cardinal.md) |
| 778803 | Authentication Bypass Using an Alternate Path or Channel | medium | $0 | [Compromise of auth via subset/superset namespace names.](778803-compromise-of-auth-via-subset-superset-namespace-names.md) |
| 1350755 | Improper Authentication - Generic | medium | $0 | [Tokenless GUI Authentication](1350755-tokenless-gui-authentication.md) |
| 859962 | Time-of-check Time-of-use (TOCTOU) Race Condition | medium | $0 | [Bypass apiserver proxy filter](859962-bypass-apiserver-proxy-filter.md) |
| 972561 | Insufficiently Protected Credentials | low | $0 | [kubeadm logs tokens before deleting them](972561-kubeadm-logs-tokens-before-deleting-them.md) |
| 1398572 | Improper Access Control - Generic | low | $0 | [Broken Link Takeover from kubernetes.io docs](1398572-broken-link-takeover-from-kubernetes-io-docs.md) |
| 802011 | Improper Authorization | low | $0 | [Grafana Improper authorization ](802011-grafana-improper-authorization.md) |
| 882923 | Uncontrolled Resource Consumption | low | $0 | [DoS for client-go jsonpath func](882923-dos-for-client-go-jsonpath-func.md) |
| 1145044 | Privilege Escalation | low | $0 | [Holes in EndpointSlice Validation Enable Host Network Hijack](1145044-holes-in-endpointslice-validation-enable-host-network-hijack.md) |
| 1092859 | Privilege Escalation | low | $0 | [KOPS documentation references domains which were not registered](1092859-kops-documentation-references-domains-which-were-not-registe.md) |
| 832593 | UI Redressing (Clickjacking) | none | $0 | [Clickjacking](832593-clickjacking.md) |
| 775531 | Improper Authentication - Generic | n/a | $0 | [No valid SPF record found](775531-no-valid-spf-record-found.md) |
| 1398617 | Improper Access Control - Generic | medium | $0 | [Broken Github Link Used in deployment docs of "github.com/kubernetes/kompose"](1398617-broken-github-link-used-in-deployment-docs-of-github-com-kub.md) |
| 1212853 | Violation of Secure Design Principles | medium | $0 | [Broken link hijacing in https://kubernetes-csi.github.io/docs/drivers.html](1212853-broken-link-hijacing-in-https-kubernetes-csi-github-io-docs.md) |
| 899103 | Man-in-the-Middle | medium | $0 | [Man in the middle leading to root privilege escalation using hostNetwork=true (CAP_NET_RAW considered harmful)](899103-man-in-the-middle-leading-to-root-privilege-escalation-using.md) |
| 833856 | Uncontrolled Resource Consumption | medium | $0 | [DoS for GCSArtifact.RealAll](833856-dos-for-gcsartifact-realall.md) |
| 1000922 | Improper Authentication - Generic | high | $0 | [Unsecured Grafana instance on https://monitoring.prow-canary.k8s.io/dashboards](1000922-unsecured-grafana-instance-on-https-monitoring-prow-canary-k.md) |
| 876751 | Cleartext Storage of Sensitive Information | medium | $0 | [Private RSA key and Server key exposed on the GitHub repository](876751-private-rsa-key-and-server-key-exposed-on-the-github-reposit.md) |
| 918243 | Fake email from <any_name>@kubernetes.io to any other email | none | $0 | [Fake email from <any_name>@kubernetes.io to any other email](918243-fake-email-from-any-name-kubernetes-io-to-any-other-email.md) |
| 764986 | Man-in-the-Middle | medium | $0 | [Man in the middle using LoadBalancer or ExternalIPs services](764986-man-in-the-middle-using-loadbalancer-or-externalips-services.md) |
| 1096907 | Uncontrolled Resource Consumption | medium | $0 | [API Server DoS (crash?) if many large resources (~1MB each) are concurrently/repeatedly sent to an external Validating WebHook endpoint](1096907-api-server-dos-crash-if-many-large-resources-1mb-each-are-co.md) |
| 970520 | Information Disclosure | high | $0 | [exposed Git Repo at http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/](970520-exposed-git-repo-at-http-api-e2e-kops-aws-canary-test-cncf-a.md) |
| 796139 | Plaintext Storage of a Password | low | $0 | [Github test clientID and clientSecret leaked](796139-github-test-clientid-and-clientsecret-leaked.md) |
| 831654 | Uncontrolled Resource Consumption | low | $0 | ["Self" DOS with large deployment and scaling](831654-self-dos-with-large-deployment-and-scaling.md) |
| 1102064 | Cleartext Storage of Sensitive Information | low | $0 | [kubectl creating secrets from stringData leaves secret in plain text](1102064-kubectl-creating-secrets-from-stringdata-leaves-secret-in-pl.md) |
| 1036886 | Privilege Escalation | medium | $0 | [Kubelet follows symlinks as root in /var/log from the /logs server endpoint ](1036886-kubelet-follows-symlinks-as-root-in-var-log-from-the-logs-se.md) |
| 995699 | NULL Pointer Dereference | medium | $0 | [csi-snapshot-controller crashes when processing VolumeSnapshot with non-existing PVC](995699-csi-snapshot-controller-crashes-when-processing-volumesnapsh.md) |
| 952771 | Cleartext Storage of Sensitive Information | medium | $0 | [CVE-2019-11250 remains in effect.](952771-cve-2019-11250-remains-in-effect.md) |
| 774872 | Information Disclosure | none | $0 | [Configuartion [Sensitive] Information Disclosure](774872-configuartion-sensitive-information-disclosure.md) |
| 864696 | Improper Authentication - Generic | none | $0 | [There is any issue No valid SPF Records](864696-there-is-any-issue-no-valid-spf-records.md) |
| 775123 | Information Disclosure | n/a | $0 | [Sensitive Information disclosure Through Config File](775123-sensitive-information-disclosure-through-config-file.md) |
| 908880 | Information Disclosure | none | $0 | [Private IP addresses Disclosure](908880-private-ip-addresses-disclosure.md) |
| 872190 | Plaintext Storage of a Password | n/a | $0 | [Plaintext storage of a password on kubernetes release bucket](872190-plaintext-storage-of-a-password-on-kubernetes-release-bucket.md) |
| 877303 | Insecure Storage of Sensitive Information | none | $0 | [Internal IP addresses range and AWS cluster region leaked in a Github repository ](877303-internal-ip-addresses-range-and-aws-cluster-region-leaked-in.md) |
| 877402 | Use of Hard-coded Credentials | none | $0 | [Hard coded Username and password in GiHub commit](877402-hard-coded-username-and-password-in-gihub-commit.md) |
