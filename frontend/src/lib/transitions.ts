import { cubicInOut } from 'svelte/easing';
import type { TransitionConfig } from 'svelte/transition';

export function float(node: Element, {
    y = 5,
    duration = 1500,
    delay = 0
}): TransitionConfig {
    return {
        duration,
        delay,
        css: (t: number) => {
            const eased = cubicInOut(t);
            return `
                transform: translateY(${(1 - eased) * y}px);
                opacity: ${eased};
            `;
        }
    };
}

export function popIn(node: Element, {
    duration = 400,
    delay = 0
}): TransitionConfig {
    return {
        duration,
        delay,
        css: (t: number) => {
            const eased = cubicInOut(t);
            return `
                transform: scale(${eased});
                opacity: ${eased};
            `;
        }
    };
}

export function slideIn(node: Element, {
    duration = 400,
    delay = 0,
    direction = 'left'
}): TransitionConfig {
    const x = direction === 'left' ? -20 : 20;
    return {
        duration,
        delay,
        css: (t: number) => {
            const eased = cubicInOut(t);
            return `
                transform: translateX(${(1 - eased) * x}px);
                opacity: ${eased};
            `;
        }
    };
}