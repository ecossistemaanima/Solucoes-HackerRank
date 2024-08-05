use std::io;

fn birthday_cake_candles(candles: &[u32]) -> usize {
    let max_height = candles.iter().cloned().max().unwrap_or(0);
    candles.iter().filter(|&&height| height == max_height).count()
}