export const colorCode = {
    'O': {
        light: "",
        hover: "",
        dark: ""
    }, 
    'Lead': {
        light: "#6ce26d66",
        hover: "#6CE26D",
        dark: "#187719"
    }, 
    'Position': {
        light: "#e19a6366",
        hover: "#E19A63",
        dark: "#894A1A"
    }, 
    'Claim': {
        light: "#eba69a66",
        hover: "#EBA69A",
        dark: "#882B1B"
    }, 
    'Counterclaim': {
        light: "#c2c34b66",
        hover: "#C2C34B",
        dark: "#7A7A29"
    }, 
    'Rebuttal': {
        light: "#aa6cce66",
        hover: "#AA6CCE",
        dark: "#5C297A"
    },
    'Evidence': {
        light: "#49b4dc66",
        hover: "#49B4DC",
        dark: "#175E78"
    }, 
    'Concluding Statement': {
        light: "#54c67666",
        hover: "#54C676",
        dark: "#297A41"
    }
}

export const queries = [
    'O', 
    'Lead', 
    'Position', 
    'Claim', 
    'Counterclaim', 
    'Rebuttal', 
    'Evidence', 
    'Concluding Statement'
];

export const queryIds = [
    'O',
    'L',
    'Pos',
    'C',
    'CC',
    'R',
    'Ev',
    'ConSt'
];

const mapTwoArrays = (arr1, arr2) => {
    return arr1.map((val, idx) => {
        return {
            [val]: arr2[idx]
        };
    });
};

export const getIdByQueryName = mapTwoArrays(queries, queryIds);

export const getQueryNameById = mapTwoArrays(queryIds, queries);