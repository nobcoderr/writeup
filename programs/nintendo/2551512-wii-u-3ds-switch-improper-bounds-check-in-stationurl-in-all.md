# [Wii U/3DS/Switch] Improper bounds check in StationURL in all NEX clients leading to remote crash/RCE

- Program: Nintendo
- Weakness / temuan: **Stack Overflow**
- Severity: low
- State: duplicate
- Bounty: $0.00
- Upvotes: 42
- Submitted: 2024-06-13
- Disclosed: 2026-08-07
- Report: https://hackerone.com/reports/2551512

## Team summary

-

## Researcher summary

`nn::nex::StationURL::Format` performs unsafe string formatting which lacks bounds checks. The `StationURL` is formatted to a string using code such as this:

```cpp
nn::nex::StationURL::Format() {
	wchar_t url[1024];
	uint offset = 0;
	uint written = 0;
	bool writeDelimiter = false;

	/* normalParams is a std::map<nn::nex::String, nn::nex::String> */
	for (auto param = normalParams.begin(); param != normalParams.end(); param++) {
		if (writeDelimiter) {
			written = swprintf(url + offset, 1024, L";");
			offset += written;
		}

		written = swprintf(url + offset, 1024, L"%ls%ls%ls", param->first, L"=", param->second);
		offset += written;
		writeDelimiter = true;
	}

	SetURL(url)
}
```

The calls to `swprintf` do not take into account the number of bytes already written into the `url` buffer, which can lead to a stack overflow given either a large enough number of parameters or a parameter with a large enough key/value. Since `StationURL`s are shared between clients, often using the server as a middleman, a remote user could send a large enough value through to another client, trigger this overflow
