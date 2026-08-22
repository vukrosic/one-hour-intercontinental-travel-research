# Metadata-only source hash manifest

Four refreshed primary pages were retrieved with `curl -L` on 2026-08-22 and recorded as byte counts plus SHA-256 digests in `source_document_hashes.csv`. `hash_manifest_check.py` validates that the IDs are registered, dates and URLs are well formed, byte counts are positive, and hashes are 64-character lowercase hexadecimal values.

This is a provenance aid, not a source archive or a claim validator. The HTML pages are not copied into the repository; pages may be dynamic or change after retrieval, and a matching hash does not establish legal force, scientific truth, or applicability to an unspecified aircraft. Refresh the manifest before relying on dated regulatory statements.
