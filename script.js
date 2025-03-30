const FIGMA_TOKEN = "YOURfigd_4IAD8mbGwd4jM8F_0StHYd0zlxJLLTxROIkYFNRU_ACCESS_TOKEN";
const BUTTON_FILE_ID = "KTzQW3JVgbusagpi94WySD";


async function getFileNodes() {
    const url = `https://api.figma.com/v1/files/${BUTTON_FILE_ID}`;
    
    const response = await fetch(url, {
        method: "GET",
        headers: {
            "X-Figma-Token": FIGMA_TOKEN
        }
    });

    const data = await response.json();
    console.log(data.document.children); // Logs all nodes
}

getFileNodes();
