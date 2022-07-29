// import { Filesystem, Directory, Encoding } from '@capacitor/filesystem'

// const saveText = async() => {
//     await Filesystem.writeFile({
//         path: 'savedText.txt',
//         data: document.getElementById("textBox").value,
//         encoding: Encoding.UTF8,
//     })
// }

// const loadText = async() => {
//     let contents = await Filesystem.readFile({
//         path: 'savedText.txt',
//         encoding: Encoding.UTF8,
//     })
//     document.getElementById("outputZone").innerHTML = contents
// }

export changeText = () => {
    document.getElementById("outputZone").innerHTML = "Snoochie Boochie"
}