import '../styles/styles'

function CommandWindow (props) {

    function setSourceSelectorValue(val) {
        const selector = document.getElementById("source-selector");
        selector.innerHTML = val;
    }

    function setTargetSelectorValue(val) {
        const selector = document.getElementById("target-selector");
        selector.innerHTML = val;
    }

    return (
        <>
            <div className='language-select-container'>
                <div className='language-selector' id='left'>
                    <button className="dropbtn" id='source-selector'>en</button>
                    <div className="language-selector-content">
                        <button onClick={() => setSourceSelectorValue('en')}>en</button>
                        <button onClick={() => setSourceSelectorValue('es')}>es</button>
                        <button onClick={() => setSourceSelectorValue('zh')}>zh</button>
                        <button onClick={() => setSourceSelectorValue('ru')}>ru</button>
                        <button onClick={() => setSourceSelectorValue('hi')}>hi</button>
                        <button onClick={() => setSourceSelectorValue('fr')}>fr</button>
                        <button onClick={() => setSourceSelectorValue('ar')}>ar</button>
                        <button onClick={() => setSourceSelectorValue('bn')}>bn</button>
                        <button onClick={() => setSourceSelectorValue('pt')}>pt</button>
                        <button onClick={() => setSourceSelectorValue('id')}>id</button>
                        <button onClick={() => setSourceSelectorValue('ur')}>ur</button>
                        <button onClick={() => setSourceSelectorValue('ja')}>ja</button>
                        <button onClick={() => setSourceSelectorValue('de')}>de</button>
                        <button onClick={() => setSourceSelectorValue('te')}>te</button>
                    </div>
                </div>
                <div className='language-selector' id='right'>
                    <button className="dropbtn" id='target-selector'>es</button>
                    <div className="language-selector-content">
                        <button onClick={() => setTargetSelectorValue('en')}>en</button>
                        <button onClick={() => setTargetSelectorValue('es')}>es</button>
                        <button onClick={() => setTargetSelectorValue('zh')}>zh</button>
                        <button onClick={() => setTargetSelectorValue('ru')}>ru</button>
                        <button onClick={() => setTargetSelectorValue('hi')}>hi</button>
                        <button onClick={() => setTargetSelectorValue('fr')}>fr</button>
                        <button onClick={() => setTargetSelectorValue('ar')}>ar</button>
                        <button onClick={() => setTargetSelectorValue('bn')}>bn</button>
                        <button onClick={() => setTargetSelectorValue('pt')}>pt</button>
                        <button onClick={() => setTargetSelectorValue('id')}>id</button>
                        <button onClick={() => setTargetSelectorValue('ur')}>ur</button>
                        <button onClick={() => setTargetSelectorValue('js')}>js</button>
                        <button onClick={() => setTargetSelectorValue('de')}>de</button>
                        <button onClick={() => setTargetSelectorValue('te')}>te</button>
                    </div>
                </div>
            </div>
            <div className='command-window'>
                <div className="Input">
                    <input type="text" id="prompt-input" className="Input-text" placeholder="Prompt Box"/>
                </div>
                <button id='prompt-submit-button' onClick={() => props.submitPrompt()}>Submit</button>
            </div>
        </>
    );
}


export default CommandWindow;