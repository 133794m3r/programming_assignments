var detectCapitalUse = function(word) {
    const re=/(^[A-Z][a-z]+$)|(^[A-Z]+$)/;
    return (word.search(re) !== -1)?True:False;
}
