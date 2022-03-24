<?php

/**
 * this is the main file of the application
 */
class Main
{
    /**
     * The sources
     * @var array|null
     */
    public ?array $sources = null;
    /**
     * The lines
     * @var array
     */
    private array $lines = [];

    public function __construct()
    {
        $this->fetchData();
        $this->writeData();
    }

    /**
     * Write the data to the file
     * @return void
     */
    private function writeData()
    {
        var_dump('Writing data to file');
        file_put_contents('ads_list.txt', implode("\n", $this->lines));
        var_dump('done');
        exit;
    }

    /**
     * Fetch the data
     * @return void
     */
    private function fetchData()
    {
        var_dump('Fetching data');
        foreach ($this->getSources() as $source) {
            var_dump('Fetching data from ' . $source);
            $lines = preg_split("/\r\n|\n|\r/", file_get_contents($source));
            $this->lines = array_merge($this->lines,
                $this->cleanLines($lines)
            );
        }
        var_dump('done fetching');
    }

    /**
     * Get clean lines
     * @param array $lines
     * @return array
     */
    public function cleanLines(array $lines): array
    {
        $clean_lines = [];
        foreach ($lines as $line) {
            $line = trim($line);
            if (!empty($line) && !substr($line, 0, 1) == "#") {
                $clean_lines[] = $line;
            }
        }
        return $clean_lines;
    }

    /**
     * Get sources
     * @return array
     */
    private function getSources(): array
    {
        if (is_null($this->sources)) {
            $this->sources = preg_split("/\r\n|\n|\r/", file_get_contents('../sources.txt'));
        }
        return $this->sources;
    }
}

new Main();