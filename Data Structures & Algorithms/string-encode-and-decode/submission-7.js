class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) { // function encode(strs: string[]): string {
        let parts = []; // let parts: string[] = []; typescript def
        for (const s of strs) {
            parts.push(`${s.length}#${s}`);
        }
        return parts.join('');
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) { // function decode(s: string): string[] {
        const res = []; // const res: string[] = [];
        let i = 0;
        const n = str.length;
        while (i < n) {
            // read length until '#'
            let j = i;
            while (j < n && str[j] !== '#') j++;
            if (j === n) break; // malformed
            const len = parseInt(str.slice(i, j), 10);
            j++; // skip '#'
            res.push(str.slice(j, j + len));
            i = j + len;
        }
        return res;
    }
}
