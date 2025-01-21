"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
// The module 'vscode' contains the VS Code extensibility API
// Import the necessary extensibility types to use in your code below
const vscode_1 = require("vscode");
const exec = require("child-process-promise").exec;
const circleChars = ["◌", "◔", "◑", "◕", "◍"];
const barChars = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"];
const recycleChars = ["♺", "♳", "♴", "♵", "♶", "♷", "♸", "♹"];
const dieChars = ["⛶", "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"];
const clockChars = ["🕛", "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚"];
const lineChars = ["⎽", "⎼", "⎻", "⎺"];
const pileChars = ["𝄖", "𝄗", "𝄘", "𝄙", "𝄚", "𝄛"];
const digitChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const circledigitChars = ["🄋", "➀", "➁", "➂", "➃", "➄", "➅", "➆", "➇", "➈"];
const negativecircledigitChars = ["🄌", "➊", "➋", "➌", "➍", "➎", "➏", "➐", "➑", "➒"];
const wanChars = ["🀆", "🀈", "🀉", "🀊", "🀋", "🀌", "🀍", "🀎", "🀏"];
const tiaoChars = ["🀆", "🀐", "🀑", "🀒", "🀓", "🀔", "🀕", "🀖", "🀗", "🀘"];
const bingChars = ["🀆", "🀙", "🀚", "🀛", "🀜", "🀝", "🀞", "🀟", "🀠", "🀡"];
const drawtypes = {
    circle: circleChars,
    bar: barChars,
    recycle: recycleChars,
    die: dieChars,
    clock: clockChars,
    line: lineChars,
    pile: pileChars,
    digit: digitChars,
    circledigit: circledigitChars,
    negativecircledigit: negativecircledigitChars,
    wan: wanChars,
    tiao: tiaoChars,
    bing: bingChars
};
const cmd = `nvidia-smi -q -d UTILIZATION | grep Gpu | sed 's/[Gpu%: ]//g'`;
// This method is called when your extension is activated. Activation is
// controlled by the activation events defined in package.json.
function activate(context) {
    return __awaiter(this, void 0, void 0, function* () {
        // Use the console to output diagnostic information (console.log) and errors (console.error).
        // This line of code will only be executed once when your extension is activated.
        console.log('Congratulations, your extension "nvidia-smi" is now active!');
        // create a new word counter
        let nvidiasmi = new NvidiaSmi(0);
        try {
            var res = yield exec(cmd, { timeout: 999 });
            var nCard = res.stdout.split("\n").filter(val => val).length;
            if (nCard > 0) {
                nvidiasmi.nCard = nCard;
                nvidiasmi.startNvidiaSmi();
            }
        }
        catch (e) {
            console.log(e);
            nvidiasmi.nCard = 0;
        }
        let updateCmd = vscode_1.commands.registerCommand("extension.nvidia-smi", () => {
            nvidiasmi.updateNvidiaSmi();
        });
        let stopCmd = vscode_1.commands.registerCommand("extension.stop_nvidia-smi", () => {
            nvidiasmi.stopNvidiaSmi();
        });
        let startCmd = vscode_1.commands.registerCommand("extension.start_nvidia-smi", () => {
            nvidiasmi.startNvidiaSmi();
        });
        context.subscriptions.push(vscode_1.workspace.onDidChangeConfiguration(() => {
            nvidiasmi.updateDrawtype();
        }));
        // Add to a list of disposables which are disposed when this extension is deactivated.
        context.subscriptions.push(nvidiasmi);
        context.subscriptions.push(updateCmd);
        context.subscriptions.push(startCmd);
        context.subscriptions.push(stopCmd);
    });
}
exports.activate = activate;
class NvidiaSmi {
    constructor(numCard) {
        this.lock = false;
        this.resetPatience();
        this.nCard = numCard;
        this.updateDrawtype();
    }
    get hasPatience() {
        return this._patience > 0;
    }
    get nCard() {
        return this._nCard;
    }
    set nCard(numCard) {
        if (numCard >= 0) {
            this._nCard = numCard;
        }
        else {
            console.log("Error: bad value of numCard!");
        }
    }
    get indicator() {
        return this._indicator;
    }
    set indicator(ind) {
        this._indicator = ind;
    }
    decPatience() {
        if (this.hasPatience) {
            this._patience -= 1;
        }
    }
    resetPatience() {
        this._patience = 5;
    }
    updateDrawtype() {
        var drawtype = vscode_1.workspace.getConfiguration("nvidia-smi").drawtype;
        this.indicator = drawtypes[drawtype];
    }
    updateNvidiaSmi() {
        return __awaiter(this, void 0, void 0, function* () {
            if (this.nCard == 0)
                return;
            if (this.lock)
                return;
            // Create as needed
            if (!this._statusBarItem) {
                this._statusBarItem = vscode_1.window.createStatusBarItem(vscode_1.StatusBarAlignment.Left, 1);
                this._statusBarItem.show();
            }
            try {
                this.lock = true;
                var res = yield exec(cmd, { timeout: 999 });
                var levels = res.stdout.split("\n").filter(val => val);
                var chars = this.indicator;
                var nlevel = chars.length - 1;
                var levelChars = levels.map(val => chars[Math.ceil((Number(val) / 100) * nlevel)]);
                this.lock = false;
            }
            catch (e) {
                console.log(e);
                this.lock = true;
            }
            // Update the status bar
            this._statusBarItem.text = levelChars.join("");
            this._statusBarItem.tooltip = levels.map(val => `${val} %`).join("\n");
        });
    }
    stopNvidiaSmi() {
        return __awaiter(this, void 0, void 0, function* () {
            if (this._interval) {
                clearInterval(this._interval);
            }
            if (this._statusBarItem) {
                this._statusBarItem.text = "";
                this._statusBarItem.tooltip = "";
            }
        });
    }
    startNvidiaSmi() {
        return __awaiter(this, void 0, void 0, function* () {
            if (this.nCard == 0)
                return;
            this._interval = setInterval(() => {
                this.updateNvidiaSmi();
            }, 2000);
        });
    }
    dispose() {
        this._statusBarItem.dispose();
        if (this._interval) {
            clearInterval(this._interval);
        }
    }
}
//# sourceMappingURL=extension.js.map