<script>
	import { Filesystem, Directory, Encoding } from '@capacitor/filesystem';

	let fileData = "Hello World!"
	let textBox

	let URI = async () => {
		console.log( await Filesystem.getUri({
			path: 'savedText.txt',
			directory: Directory.Data,
		}))

	}

	const saveText = async () => {
		await Filesystem.writeFile({
			path: 'savedText.txt',
			data: textBox.value,
			directory: Directory.Data,
			encoding: Encoding.UTF8,
		})
	}

	const loadText = async () => {
		const file = await Filesystem.readFile({
			path: 'savedText.txt',
			directory: Directory.Data,
			encoding: Encoding.UTF8,
		})
		console.log(file)
		fileData = file.data
	}

	const updateText = () => {
		fileData = textBox.value
	}
</script>

<h1 id="outputZone">{fileData}</h1>
<input type="text" bind:this={textBox}>
<input type="button" value="Save Text" on:click={saveText}>
<input type="button" value="Load Text" on:click={loadText}>
<input type="button" value="Update Text" on:click={updateText}>
<input type="button" value="File URI" on:click={URI}>
