import React, { Fragment, useContext, useEffect, useState } from 'react';
import { AllContext } from '../../App/MyContext';
import { ModalThemeChanged } from '../Modals/ModalThemeChanged';

function Main() {
    const { ls, lf, s, f, Icons } = useContext(AllContext);
    const icons = new Icons();

    return (
        <Fragment>
            <div className="flex w-full p-8">
                <button className='rounded-lg bg-blue-500 text-white p-4' onClick={f.petition}>
                    Test
                </button>
            </div>
        </Fragment>
    )
}

export { Main };
